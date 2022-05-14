const Message = require("../models/Message")
const fs = require("fs")
const generateRange = require("../helpers/numRange")

const get = async (req, res) => {
    const messages = await Message.findAll()
    res.render("range", {flash : req.flash(), messages})
}

const post = async(req, res) => {
    const numbers = generateRange.generate(req.body.ranges)
    fs.writeFile("./public/uploads/range.txt", numbers.join("\n"),(err, fileR) => {
        if(!err){
            res.download("./public/uploads/range.txt", `ranges-${req.body.ranges}.txt`)
        }else{
            res.send(`ERROR !!\n\n\n\n${err}`)
        }
    })

}

module.exports = {get, post}