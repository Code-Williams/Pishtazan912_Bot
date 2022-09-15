from fileinput import filename
import utils, os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

numbers = os.listdir("posts")
link = "https://my.uupload.ir/dl/aGk0e027"

numbers_log = {}

for number in numbers:
    if(number.endswith(".jpg")):
        file_name = number
        number = utils.check_number(number.split(".")[0], driver)
        if number : 
            utils.write_description(number, link, driver)
            print(f"Number {number} deleted")
            numbers_log[file_name.split(".")[0]] = "Found"
        else:
            os.remove(f"posts/{file_name}")
            print(f"Number {filename.split('.')[0]} deleted")
            numbers_log[filename.split(".")[0]] = "Not Found"

