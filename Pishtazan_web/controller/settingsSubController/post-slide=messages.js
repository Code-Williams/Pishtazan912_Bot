const Setting = require("../../models/Settings")

const execute = async (req, res) => {
    console.log("running")
    const settings = await Setting.findAll()

    if(req.body.sleepTime !== settings.find(s => s.name == "sleep time").value){
        const findSleepTime = await Setting.findOne({
            where : {
                name : "sleep time"
            }
        })

        await findSleepTime.update({
            value : req.body.sleepTime
        })
    }

    if(req.body.tryTime !== settings.find(s => s.name == "try time").value){
        const findTryTime = await Setting.findOne({
            where : {
                name : "try time"
            }
        })

        await findTryTime.update({
            value : req.body.tryTime
        })
    }

    if(req.body.message !== settings.find(s => s.name == "message").value){
        const findMessage = await Setting.findOne({
            where :{
                name : "message"
            }
        })

        await findMessage.update({
            value : req.body.message
        })
    }
}

module.exports = execute