import webbrowser, pyautogui, time, os, datetime
import pandas as pd


def log(number, message):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_file = open(f"log-{log_date}.txt", "a")
    log_file.write("\n" + f"\nNumber : {number}\nDate : {log_date}\nTime : {log_time}\nMessage : {message}\n" + ("-" * 20))
    log_file.close()


def send_message(number, message, sleep_time, driver):
    driver.get(f"https://web.whatsapp.com/send?phone={number}&source=&data=#")

    # is_number_not_found = driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
    # if not is_number_not_found or not is_number_not_found.text == "Phone number shared via url is invalid.":

    # time.sleep(sleep_time)
    # pyautogui.send_keys(message)
    # pyautogui.press("enter")
    # log(number, message)
    # time.sleep(1)

    time.sleep(float(sleep_time))

    loop_count = 0
    while True:
        try:
            chat_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
            chat_input.click()
            chat_input.send_keys(message)
            print(f"Message for [ {number} ] has been sent.")
            break
        except Exception as e:
            loop_count += 1
            if loop_count >= 3:
                print(f"Number [ {number} ] is not defined.")
                break
            time.sleep(3)

    time.sleep(0.3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
    time.sleep(1)


def read_excel_data(excel_file):
    file_e = pd.read_excel(excel_file, index_col=None, header=None)
    numbers = []
    for number in file_e.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))
    return numbers
