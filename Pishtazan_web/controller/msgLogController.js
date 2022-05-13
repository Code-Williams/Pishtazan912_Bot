const Messages = require("../models/Message")

const get = async (req, res) => {
    const messages = await Messages.findAll()
    res.render("logs", {messages, flash : req.flash()})
}

module.exports = {get}