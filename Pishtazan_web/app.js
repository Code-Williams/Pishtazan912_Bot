const express = require("express");
const bodyParser = require("body-parser");
const flash = require("connect-flash");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const passport = require("passport");

const PORT = 3000;
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("views", __dirname + "/views");
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");

// GET requests handlers
const routes = require("./routes");
app.use("/", routes);

// POST requests handlers
const apiRoutes = require("./routes/api");
app.use("/api", apiRoutes);

app.listen(PORT, () => {
  console.log(`Server is listening to ${PORT}`);
});
