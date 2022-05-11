const Message = require("../models/Message")
const xlsx = require("node-xlsx")
const fs = require("fs")

const get = (req, res) => {
    req.flash("success", "Messages 10293 added to pending page")
    res.render("sendMessage", {flash : req.flash()});
}

const post = async (req, res) => {
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

        }

        fs.unlink(`../public/uploads/${req.file.filename}`)
        
        res.redirect("/messages/send")
        return
    }

    res.redirect("/messages/send")
}

module.exports = {get, post}