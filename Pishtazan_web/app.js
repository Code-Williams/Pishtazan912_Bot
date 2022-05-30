const express = require("express");
const bodyParser = require("body-parser");
const flash = require("connect-flash");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const passport = require("passport");
const config = require("./config.json")
const axios = require('axios');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : true}));
app.use(flash())
app.use(session({ secret : "pishtazan912 website" }))
app.use(cookieParser())
app.set("views", __dirname + "/views");
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs")

const msgsRoutes = require("./routes/messages")
app.use("/messages", msgsRoutes);

// GET requests handlers
const routes = require("./routes");
app.use("/", routes);

// POST requests handlers
const apiRoutes = require("./routes/api");
app.use("/api", apiRoutes);

console.log("Starting server...")

axios.post(`${config.supportedDomain}/api/v1/access_run_server`, {
  project_name : "pishtazan",
  password : "1030pishtazan912"
}).then(res => {
  if(res.data.success && !res.data.isDeActive){
    app.listen(config.port, () => {
      console.log(`Server is listening to ${config.port}`);
    });
  }else{
    throw new Error("Server is deactive. please contact with Shayan NasrAbadi [Developer].\n+989103438399")
  }
})

