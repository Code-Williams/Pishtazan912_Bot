const Message = require("../models/Message")

const post = async(req, res) => {
    const findMessage = await Message.findOne({
        where :{
            id : req.params.id
        }
    })

    if(findMessage){
        await Message.destroy({
            where :{
                id : req.params.id
            }
        })

        req.flash("success", `Successfully deleted message id ${req.params.id}`)
        res.redirect("/messages/log")
    }else{
        req.flash("danger", `Can't find message id ${req.params.id}`)
        res.redirect("/messages/log")
    }
}

module.exports = {post}