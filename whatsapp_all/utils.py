import webbrowser, pyautogui, os, datetime, time
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

def start_setup(driver):
    driver.get("https://web.whatsapp.com")
    input("Scan QR then enter to start.")

def send_file(driver, file_path):
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input").send_keys(f"C:\\Users\\Administrator\\Desktop\\Pishtazan912_Bot\\Pishtazan_web\\public\\uploads\\{file_path}")
        return True
    except:
        return False

def send_message(number, message, sleep_time, driver):
    trying_send = 0
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={number}&source=&data=#&text={message}")

        time.sleep(int(sleep_time))

        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()

        time.sleep(0.5)

        return True

    except Exception as e:
        return False

def read_excel_data(excel_file):
    excel_file = pd.read_excel(excel_file, index_col=None, header=None)

    numbers = []

    for number in excel_file.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))

    return numbers