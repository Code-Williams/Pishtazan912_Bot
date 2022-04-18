import webbrowser, pyautogui, time, os, datetime
import pandas as pd


def log(number, message):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_file = open(f"log-{log_date}.txt", "a")
    log_file.write("\n" + f"\nNumber : {number}\nDate : {log_date}\nTime : {log_time}\nMessage : {message}\n" + ("-" * 20))
    log_file.close()


def send_message(number, message, sleep_time, driver):
    driver.get(f"https://wa.me/{number}")
    pyautogui.press("escape")
    find_continue_button = driver.find_element_by_xpath('//*[@id="action-button"]')

    if find_continue_button:
        find_continue_button.click()

    time.sleep(float(sleep_time))

    while True:
        try:
            chat_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
            chat_input.click()
            chat_input.send_keys(message)
            break
        except Exception as e:
            time.sleep(3)

    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()


def read_excel_data(excel_file):
    file_e = pd.read_excel("excel.xlsx", index_col=None, header=None)
    numbers = []
    for number in file_e.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))
    return numbers