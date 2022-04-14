num = input("Pish shomare ra vared konid : ")
nums = []
if not num.startswith("09"):
    "09" + num

if not num.startswith("0"):
    "0" + num

lenghts = 11 - len(num) - 1
nums_for_loop = ""

if lenghts >= 1:
    for numbers in range(lenghts):
        nums_for_loop += "9"

for numLoop in range(0, int(nums_for_loop) + 1):
        lenghts_for_0 = len(nums_for_loop) - len(str(numLoop))
        zeros = ""
        for zero in range(lenghts_for_0 + 1):
            zeros += "0"
        
        nums.append(num + str(zeros) + str(numLoop))

print(nums)