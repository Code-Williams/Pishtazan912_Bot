const Goal = require("../../models/Goals")

const execute = async (req, res) => {
    console.log(2)
    if(req.body.resetGoal !== ""){
        console.log(3)

        const goals = await Goal.findAll()

        if(req.body.sentMessage !== goals.find(g => g.name == "sent messages").value){
            const findSentMessage = await Goal.findOne({
                where : {
                    name : "sent messages"
                }
            })

            await findSentMessage.update({
                goal : req.body.sentMessage
            })
        }
        
        if(req.body.allMessage !== goals.find(g => g.name == "all messages").value){
            const findAllMessage = await Goal.findOne({
                where : {
                    name : "all messages"
                }
            })

            await findAllMessage.update({
                goal : req.body.allMessage
            })
        }

    }else{

        const findSentGoal = await Goal.findOne({
            where : {
                name : "sent done",
            }
        })

        const findAllGoal = await Goal.findOne({
            where : {
                name : "all done"
            }
        })

        findSentGoal.update({ goal : 0 })
        findAllGoal.update({ goal : 0 })
        
    }
}

module.exports = execute