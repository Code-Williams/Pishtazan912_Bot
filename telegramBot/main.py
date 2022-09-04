import utils, os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

numbers = os.listdir("posts")
link = ""

numbers_log = {}

for number in numbers:
    if(number.endswith(".jpeg")):
        file_name = number
        number = utils.check_number(number.replace(".jpeg", ""), driver)
        if number : 
            utils.write_description(number, link, driver)
            print(f"Number {number} deleted")
            numbers_log[file_name.replace('.jpeg', '')] = "Found"
        else:
            os.remove(f"posts/{file_name}")
            print(f"Number {file_name.replace('.jpeg', '')} deleted")
            numbers_log[file_name.replace('.jpeg', '')] = "Not Found"

log = open("log.txt", "w")
log.write(numbers_log)
log.close()