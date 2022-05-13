const { DataTypes } = require("sequelize");
const db = require("../configs/db");

const Message = db.define(
  "messages",
  {
    id: {
      type: DataTypes.NUMBER,
      primaryKey: true,
      autoIncrement: true,
    },

    number: {
      type: DataTypes.STRING,
    },

    message: {
      type: DataTypes.STRING,
    },

    stats: {
      type: DataTypes.STRING,
    },

    activity_time: {
      type : DataTypes.TEXT
    }
  },
  {
    timestamps: false,
  }
);

module.exports = Message;
