import webbrowser, pyautogui, time, os, datetime
import pandas as pd

counter = 0

def log(number, message):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_file = open("log.txt", "a")
    log_file.write("\n" + f"\nNumber : {number}\nDate : {log_date}\nTime : {log_time}\nMessage : {message}\n" + ("-" * 20))
    log_file.close()

def send_message(number, message, sleep_time):
    global counter

    if counter == 2:
        os.system("pkill firefox")
        webbrowser.open("https://google.com")
        time.sleep(5)
        counter = 0

    webbrowser.open(f"https:/wa.me/{number}")
    time.sleep(int(sleep_time))
    pyautogui.write(message)
    pyautogui.press("enter")
    log(number, message)
    counter += 1

def read_excel_data(excel_file):
    file_e = pd.read_excel("excel.xlsx", index_col=None, header=None)
    numbers = []
    for number in file_e.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))
    return numbers