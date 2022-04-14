import utils

numbers = []

while True:
    req = input("Enter a number or 'done' to exit: ")
    if req.lower() != "done":
        num = input("Enter a number: ")
        numbers.append(num)
    else:
        break

time = input("Enter time [Seconds]: ")

message_file = open("message.txt", "r")
message = message_file.read()
message_file.close()

for number in numbers:
    utils.send_message(number, message, time)