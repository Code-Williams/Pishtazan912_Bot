const { DataTypes } = require("sequelize");
const db = require("../configs/db");

const Goals = db.define(
  "goals",
  {
    id: {
      type: DataTypes.NUMBER,
      primaryKey: true,
      autoIncrement: true,
    },

    name: {
      type: DataTypes.STRING,
    },

    goal: {
      type: DataTypes.STRING,
    },
  },
  {
    timestamps: false,
  }
);

module.exports = Goals;
