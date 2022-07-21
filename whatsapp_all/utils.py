import webbrowser, pyautogui, os, datetime, time
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, init
import pandas as pd

init()

def log(number, message):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_file = open(f"log-{log_date}.txt", "a")
    log_file.write("\n" + f"\nNumber : {number}\nDate : {log_date}\nTime : {log_time}\nMessage : {message}\n" + ("-" * 20))
    log_file.close()


def send_message(number, message, sleep_time, img_path, pdf_path, driver):
    trying_send = 0
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={number}&source=&data=#")

        time.sleep(float(sleep_time))

        is_message_sent = False
        try:
            chat_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
            if chat_input:
                #chat_input.click()
                chat_input.send_keys(message)
                is_message_sent = True
            else:
                return 'cant send'
        except Exception as e:
            try:
                is_number_invalid = driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                if is_number_invalid and is_number_invalid.text == "Phone number shared via url is invalid.":
                    return False
                return 'not defined'
            except:
                return 'not defined'

        if is_message_sent:
            time.sleep(0.2)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
            time.sleep(1)
            # finding and sending pdf file
            if pdf_path and not pdf_path == "":
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input").send_keys(f"C:\\Users\\Administrator\\Desktop\\Pishtazan912_Bot\\Pishtazan_web\\public\\uploads\\{pdf_path}")
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]").click()

            # finding and sending picture
            if img_path and not img_path == "":
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input").send_keys(f"C:\\Users\\Administrator\\Desktop\\Pishtazan912_Bot\\Pishtazan_web\\public\\uploads\\{img_path}")
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]").click()

            time.sleep(1)
            return True
    except Exception as e:
        print(e)
        try:
            is_number_invalid = driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
            if is_number_invalid.text == "Phone number shared via url is invalid.":
                return False
            return 'cant send'
        except:
            return 'cant send'

def read_excel_data(excel_file):
    file_e = pd.read_excel(excel_file, index_col=None, header=None)
    numbers = []
    for number in file_e.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))
    return numbers
