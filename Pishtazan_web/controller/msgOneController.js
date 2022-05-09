const Messages = require("../models/Message")

const get = async (req, res) => {
    const message = await Messages.findOne({
        where : {
            id : req.params.id
        }
    })

    if(message){
        res.render("oneMessage", {message})
    }else{
        res.render("404")
    }
}

module.exports = {get}