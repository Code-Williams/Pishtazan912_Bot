const express = require("express");
const Router = new express.Router();

const logController = require("../controller/msgLogController")
Router.get("/messages/log", logController.get)

module.exports = Router