const Message = require("../models/Message")
const Setting = require("../models/Settings")

const get = async (req, res) => {
    const messages = await Message.findAll();
    const defMessage = await Setting.findOne({
        where : {
            name : "message"
        }
    }) || ""

    res.render("sendOneMessage", {flash : req.flash(), messages, defMessage});
}

const post = async (req, res) => {
    if(req.body.password && req.body.password == "pishtazan912"){
        if(req.body.number.startsWith("98")) req.body.number = req.body.number.substring(2);
        if(req.body.number.startsWith("9")) req.body.number = "+98" + req.body.number;
        if(req.body.number.startsWith("0")) req.body.number = "+98" + req.body.number.substring(1);

        let date = new Date();
        date = `${date.getFullYear()}/${date.getMonth()}/${date.getDay()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
        
        await Message.create({
            number: req.body.number,
            message: req.body.message,
            stats: "pending",
            activity_time : date
        })

        req.flash("success", `Successfully inserted ${req.body.number} into pending list`)

    }else{
        req.flash("danger", "Password is incorrect")
    }
        
    res.redirect("/messages/send/one")
}

module.exports = {get, post}