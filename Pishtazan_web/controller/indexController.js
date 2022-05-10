const Messages = require("../models/Message");
const Goals = require("../models/Goals");
const Setting = require("../models/Settings")

const get = async (req, res) => {
  let sending = await Setting.findOne({
    where : {
      name : "av-checking"
    }
  });
  const messages = await Messages.findAll();
  const goals = await Goals.findAll();
  
  res.render("index", { messages, goals, sending : sending.value });
};

module.exports = { get };
