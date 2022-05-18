import pandas as pd

num = input("Pish shomare ra vared konid : ")
nums = []

if num.startswith("09"):
   num = num.replace("09", "9") 

if num.startswith("+98"):
    num = num.replace("+98", "")

if num.startswith("0098"):
    num = num.replace("0098", "")

if num.startswith("9"):
    num = "+98" + num

lenghts = 13 - len(num)
nums_for_loop = ""

if (lenghts - 1) >= 1:
   nums_for_loop = "9" * (lenghts - 1)

for numLoop in range(0, int("9" + nums_for_loop) + 1):
        lenghts_for_0 = len(nums_for_loop) - len(str(numLoop))
        zeros = ""
        for zero in range(lenghts_for_0 + 1):
            zeros += "0"
        
        created_number = num + str(zeros) + str(numLoop)
        nums.append(created_number)
        print(f"Number {len(nums)} is : {created_number}")

print("Numbers lenght is : ", len(nums))

save_to_excel = input("Save this to excel file ?")
if "y" in save_to_excel.lower() and not "n" in save_to_excel.lower():
    
    print("Saving numbers...")
    df = pd.DataFrame(nums)
    writer = pd.ExcelWriter(f'{num}-numbers.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    print("Numbers saved successfully.")

else:
    print("Save numbers to excel file cancelled [Dont enter N in last question]")
