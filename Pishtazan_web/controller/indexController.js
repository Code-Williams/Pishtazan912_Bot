const Messages = require("../models/Message");
const Goals = require("../models/Goals");

const get = async (req, res) => {
  const messages = await Messages.findAll();
  const goals = await Goals.findAll();

  res.render("index", { messages, goals });
};

module.exports = { get };
