const express = require("express");
const Router = new express.Router();

const indexController = require("../controller/indexController");
Router.get("/", indexController.get);

const messageController = require("../controller/msgLogController")
Router.get("/messages/log", messageController.get);

// const messagesRouter = require("./messagesRoute");
// Router.use("/messages/log" , messagesRouter);

module.exports = Router;
