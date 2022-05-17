const express = require("express")
const upload = require("../helpers/uploader")
const Router = new express.Router()

const messageController = require("../controller/msgLogController")
Router.get("/log", messageController.get);

const sendMessageController = require("../controller/msgSendController")
Router.get("/send", sendMessageController.get);
Router.post("/send", upload.single("file"), sendMessageController.post)

const oneMessageController = require("../controller/msgOneController")
Router.get("/:id", oneMessageController.get);

const deleteMessageController = require("../controller/msgDeleteController")
Router.post("/:id/delete", deleteMessageController.post)

const sendOneMessageController = require("../controller/msgSendOneController")
Router.get("/send/one", sendOneMessageController.get);
Router.post("/send/one", sendOneMessageController.post);

module.exports = Router