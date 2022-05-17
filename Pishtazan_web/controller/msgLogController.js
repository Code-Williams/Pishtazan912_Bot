const Messages = require("../models/Message")

const get = async (req, res) => {
    const messages = await Messages.findAll()
    res.render("logs", {messages, flash : req.flash()})
}

const post = async (req, res) => {
    if(req.body['pendings'] == ''){
        const messages = await Messages.findAll({
            where : {
                stats : "pending"
            }
        })
        
        messages.forEach(async message => {
            await message.destroy()
        })
        
        req.flash("success", "Successfully deleted all pendings")
    }else if(req.body['all'] == ''){
        const messages = await Messages.findAll()
        
        messages.forEach(async message => {
            await message.destroy()
        })
        
        req.flash("success", "Successfully deleted all log")
    }
    res.redirect("/messages/log")
}

module.exports = {get, post}