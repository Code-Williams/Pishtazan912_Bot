const express = require("express");
const Router = new express.Router();
const upload = require("../helpers/uploader")

const indexController = require("../controller/indexController");
Router.get("/", indexController.get);

const generateRangeController = require("../controller/generateRangeController")
Router.get("/range", generateRangeController.get);
Router.post("/range", generateRangeController.post);

const settingsController = require("../controller/settingsController")
Router.get("/settings", settingsController.get)
Router.post("/settings", settingsController.post)
Router.post("/settings/files", upload.single("file"), settingsController.postFile)
// const messagesRouter = require("./messagesRoute");
// Router.use("/messages/log" , messagesRouter);

module.exports = Router;
