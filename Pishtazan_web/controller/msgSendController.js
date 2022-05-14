const Message = require("../models/Message")
const numGenerator = require("../helpers/numRange")
const Setting = require("../models/Settings")
const fs = require("fs")
const xlsx = require("node-xlsx")

const get = async (req, res) => {
    const messages = await Message.findAll();
    const defMessage = await Setting.findOne({
        where : {
            name : "message"
        }
    }) || ""

    res.render("sendMessage", {flash : req.flash(), messages, defMessage});
}

const post = async (req, res) => {
    let date = new Date();
    date = `${date.getFullYear()}/${date.getMonth()}/${date.getDay()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`

    if(req.file && req.file.filename){
        if(req.body.password && req.body.password == "pishtazan912"){

            let dir;
            try {
                dir = __dirname.replace("\\controller", "") + "\\public\\uploads\\"
                fs.readdirSync(dir)
            } catch (error) {
                dir = __dirname.replace("/controller", "") + "/public/uploads/"
                fs.readdirSync(dir)
            }

            if(req.file.filename.endsWith(".xlsx")){

                var numbers = await xlsx.parse(dir + req.file.filename);
                
                for(const i of numbers[0].data){
                    if (i[0].length >= 10 && i[0].length <= 13) {
                        if(i[0].startsWith("9")) i[0] = "+98" + i[0];
                        if(i[0].startsWith("0")) i[0] = "+98" + i[0].substring(1);

                        await Message.create({
                            number: i[0],
                            message: req.body.message,
                            stats: "pending",
                            activity_time : date
                        })
                    }
                }

                req.flash("success", `Successfully inserted ${numbers[0].data.length} numbers into pending list`)

            }else if(req.file.filename.endsWith(".txt")){

                const numbers = fs.readFileSync(dir + req.file.filename, {encoding : "utf-8"}).split("\n")

                numbers.forEach(async number => {

                    if (number.length >= 10 && number.length <= 13) {
                        if(number.startsWith("9")) number = "+98" + number;
                        if(number.startsWith("0")) number = "+98" + number.substring(1);

                        await Message.create({
                            number: number,
                            message: req.body.message,
                            stats: "pending",
                            activity_time : date
                        })
                    }
                    
                })

                req.flash("success", `Successfully inserted ${numbers.length} numbers into pending list`)

            }

        }else{
            req.flash("danger", "Password is incorrect")
        }
        
        res.redirect("/messages/send")
        return
    }else if(req.body.range){
        const numbers = numGenerator.generate(req.body.range)
        numbers.forEach(async number => {
            await Message.create({
                number,
                message : req.body.message,
                stats : "pending",
                activity_time : date
            })
        })

        req.flash("success", `Successfully inserted ${numbers.length} numbers into pending list`)
        res.redirect("/messages/send")
        return
    }

    req.flash("danger", "File not found")
    res.redirect("/messages/send")
}

module.exports = {get, post}