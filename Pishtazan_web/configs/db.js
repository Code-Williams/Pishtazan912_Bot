const sequelize = require("sequelize");

const db = new sequelize("pishtazan", "root", "shayanwilliams", {
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
