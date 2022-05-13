const express = require("express");
const Router = new express.Router();
const upload = require("../helpers/uploader")

const indexController = require("../controller/indexController");
Router.get("/", indexController.get);

const messageController = require("../controller/msgLogController")
Router.get("/messages/log", messageController.get);

const sendMessageController = require("../controller/msgSendController")
Router.get("/messages/send", sendMessageController.get);
Router.post("/messages/send", upload.single("file"), sendMessageController.post)

const oneMessageController = require("../controller/msgOneController")
Router.get("/messages/:id", oneMessageController.get);

const deleteMessageController = require("../controller/msgDeleteController")
Router.post("/messages/:id/delete", deleteMessageController.post)

// const messagesRouter = require("./messagesRoute");
// Router.use("/messages/log" , messagesRouter);

module.exports = Router;
