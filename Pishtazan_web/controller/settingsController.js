const Setting = require("../models/Settings")
const Goal = require("../models/Goals")
const subController_goal = require("./settingsSubController/post-slide=goal")
const subController_message = require("./settingsSubController/post-slide=messages")

const get = async (req, res) => {
    const settings = await Setting.findAll();
    const goals = await Goal.findAll();

    res.render("settings", {flash : req.flash(), settings, goals})
}

const post = async (req, res) => {
    if(req.query.slide && req.query.slide == "messages"){
        await subController_message(req, res)
    }else if(req.query.slide && req.query.slide == "goal"){
        await subController_goal(req, res)
    }

    req.flash("success", "Settings Updated Successfully")
    res.redirect("/settings")
}

const postFile = async (req, res) => {
    const file = req.file
    console.log(1)
    
    if(file && !file.filename.endsWith(".pdf")){
        const settings = await Setting.findOne({
            where : {
                name : "img"
            }
        });

        settings.update({
            value : file.filename
        })
    }else if (file){
        const settings = await Setting.findOne({
            where : {
                name : "pdf"
            }
        })

        settings.update({
            value : file.filename
        })
    }

    req.flash("success", "Settings Updated Successfully")
    res.redirect("/settings")
}

module.exports = {get, post, postFile}