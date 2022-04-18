import utils
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

time = input("Enter time [Seconds]: ")
file_name = input("Enter file name : ")
numbers = utils.read_excel_data(file_name)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com")

input("Scan QR code and hit enter")

for number in numbers:
    utils.send_message(number, "Hi!", time, driver)
