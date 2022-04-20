import utils, sys
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

time = input("Enter time [Seconds]: ")

if time == "about":
    print("Developer : Shayan Nasrabadi [Wil1i]\nGitHub : https://github.com/Code-Williams")
    sys.exit()

numbers = []
while True:
    new_number = input("Enter number ['done' for continue] : ")
    if not new_number.lower() == "done":
        
        if new_number.startswith("9"):
            new_number = new_number.replace("9", "+989")
        elif new_number.startswith("09"):
            new_number = new_number.replace("09", "+989")
        elif new_number.startswith("0098"):
            new_number = new_number.replace("0098", "+98")
        
        new_number.append(new_number)

    else:
        break

message_file = open("message.txt", "r", encoding="UTF-8")
message = message_file.read()
message_file.close()
print(f"Message is : {message}")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com")

input("Scan QR code and hit enter")

for number in numbers:
    utils.send_message(number, message, time, driver)
