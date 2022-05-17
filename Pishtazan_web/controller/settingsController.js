const Setting = require("../models/Settings")

const get = async (req, res) => {
    const settings = await Setting.findAll();

    res.render("settings", {flash : req.flash(), settings})
}

const post = async (req, res) => {
    if(req.body.sleepTime !== ""){
        const findSleepTime = await Setting.findOne({
            where : {
                name : "sleepTime"
            }
        })

        await findSleepTime.update({
            value : req.body.sleepTime
        })
    }else if(req.body.tryTime !== ""){
        const findTryTime = await Setting.findOne({
            where : {
                name : "try time"
            }
        })

        await findTryTime.update({
            value : req.body.tryTime
        })
    }else if(req.body.message !== ""){
        const findMessage = await Setting.findOne({
            where :{
                name : "message"
            }
        })

        await findMessage.update({
            value : req.body.message
        })
    }

    req.flash("success", "Settings Updated Successfully")
    res.redirect("/settings")
}

module.exports = {get, post}