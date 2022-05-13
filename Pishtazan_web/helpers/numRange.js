const generate = (num) => {
    if(num.startsWith("98")) num = num.substring(2);
    if(num.startsWith("9")) num = "+98" + num
    if(num.startsWith("0")) num = "+98" + num.substring(1)

    let neededNums = 13 - num.length
    let loopNum = ""
    let count = 0
    let generatedNums = []

    while(loopNum.length < neededNums){
        loopNum += "9"
    }

    while (count <= parseInt(loopNum)) {
        let zeros = ""
        let neededZeros = 13 - (num.length + count.toString().length)
        while(zeros.length < neededZeros){
            zeros += "0"
        }

        generatedNums.push(num.toString() + zeros.toString() + count.toString())
        
        count ++
    }

    return generatedNums
}

module.exports = {generate}