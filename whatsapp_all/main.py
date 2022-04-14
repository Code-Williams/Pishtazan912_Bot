import utils

time = input("Enter time [Seconds]: ")
file_name = input("Enter file name : ")
numbers = utils.read_excel_data(file_name)

for number in numbers:
    utils.send_message(number, "Hi!", time)