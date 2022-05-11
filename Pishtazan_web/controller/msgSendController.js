const Message = require("../models/Message")
const xlsx = require("node-xlsx")
const fs = require("fs")

const get = async (req, res) => {
    const messages = await Message.findAll();

    res.render("sendMessage", {flash : req.flash(), messages});
}

const post = async (req, res) => {
    console.log("post")
    if(req.file && req.file.filename){
        if(req.body.password && req.body.password == "pishtazan912"){

            const dir = __dirname.replace("/controller", "") + "/public/uploads/"
            var numbers = await xlsx.parse(dir + req.file.filename);
            
            for(const i of numbers[0].data){
                if (i[0].length >= 10 && i[0].length <= 13) {
                    await Message.create({
                        number: i[0],
                        message: req.body.message,
                        stats: "pending"
                    })
                }
            }

            req.flash("success", `Successfully inserted ${numbers[0].data.length} numbers into pending list`)
        }else{
            req.flash("danger", "Password is incorrect")
        }
        
        res.redirect("/messages/send")
        return
    }

    req.flash("danger", "File not found")
    res.redirect("/messages/send")
}

module.exports = {get, post}