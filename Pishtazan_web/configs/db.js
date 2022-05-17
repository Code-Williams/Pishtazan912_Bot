const sequelize = require("sequelize");
const config = require("../config.json")

const db = new sequelize(config.db.name, config.db.user, config.db.password, {
  host: "localhost",
  dialect: "mysql",
});

try {
  db.authenticate();
  console.log(`DatBase is running`);
} catch (e) {
  console.log(`DataBase connection error `, e);
}

module.exports = db;
