import webbrowser, pyautogui, time, os, datetime
import pandas as pd


def log(number, message):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_file = open(f"log-{log_date}.txt", "a")
    log_file.write("\n" + f"\nNumber : {number}\nDate : {log_date}\nTime : {log_time}\nMessage : {message}\n" + ("-" * 20))
    log_file.close()


def send_message(number, message, sleep_time, driver):
    trying_send = 0
    while True:
        try:
            driver.get(f"https://web.whatsapp.com/send?phone={number}&source=&data=#")

            time.sleep(float(sleep_time))

            loop_count = 0
            is_message_sent = True
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
                        is_message_sent = False
                        break
                    time.sleep(3)

            if is_message_sent:
                time.sleep(0.2)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
                time.sleep(1.5)
            break
        except:
            trying_send += 1
            if trying_send == 10:
                print("[ERROR] Can't send message to this number after 10 try, skipping this number.")
            print("[ERROR] Message not send, wait for 1 minute")
            time.sleep(60)

def read_excel_data(excel_file):
    file_e = pd.read_excel(excel_file, index_col=None, header=None)
    numbers = []
    for number in file_e.iterrows():
        numbers.append("+98" + str(number[1].tolist()).replace("[","").replace("]",""))
    return numbers
