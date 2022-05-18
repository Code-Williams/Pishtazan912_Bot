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
    console.log(req.body)
    if(req.query.slide && req.query.slide == "messages"){
        await subController_message(req, res)
    }else if(req.query.slide && req.query.slide == "goal"){
        await subController_goal(req, res)
    }

    req.flash("success", "Settings Updated Successfully")
    res.redirect("/settings")
}

module.exports = {get, post}