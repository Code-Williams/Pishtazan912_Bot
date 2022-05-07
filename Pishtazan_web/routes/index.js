const express = require("express");
const Router = new express.Router();

const indexController = require("../controller/indexController");
Router.get("/", indexController.get);

module.exports = Router;
