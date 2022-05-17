const Messages = require("../models/Message")

const get = async (req, res) => {
    const messages = await Messages.findAll()
    res.render("logs", {messages, flash : req.flash()})
}

const post = async (req, res) => {
    const messages = await Messages.findAll({
        where : {
            stats : "pending"
        }
    })

    messages.forEach(async message => {
        await message.destroy()
    })

    req.flash("success", "Successfully deleted all pendings")
    res.redirect("/messages/log")
}

module.exports = {get, post}