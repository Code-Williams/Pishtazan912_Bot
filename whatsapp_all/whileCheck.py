import utils, sys, mysql.connector, time, config
from colorama import Fore, init
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

init()

mydb = mysql.connector.connect(
    host = "localhost",
    user = config.user,
    password = config.password,
    database = config.database
)

cursor = mydb.cursor()

if mydb:
    print("Connected to DataBase")
else:
    print("Can't connect to DataBase")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com")

def check_db():
    cursor.execute(f"UPdATE settings SET value = 'Yes' WHERE name = 'av-checking'")
    mydb.commit()

    while True:
        print("-"*30)
        cursor.execute("SELECT * FROM messages WHERE stats = 'pending' LIMIT 1")
        res = cursor.fetchall()


        if not res:
            break

        while True:

            cursor.execute(f"UPDATE messages SET stats = 'sending' WHERE id={res[0][0]}")
            mydb.commit()

            cursor.execute("SELECT * FROM settings WHERE name = 'sleep time'")
            sleepTime = cursor.fetchall()[0][2]

            cursor.execute("SELECT * FROM settings WHERE name = 'try time'")
            tryTime = cursor.fetchall()[0][2]

            cursor.execute("SELECT * FROM settings WHERE name = 'img'")
            img_path = cursor.fetchall()[0][2]

            cursor.execute("SELECT * FROM settings WHERE name = 'pdf'")
            pdf_path = cursor.fetchall()[0][2]

            id, number, message, stats, activity_time = res[0]
            print("Start sending" + Fore.GREEN + number + Fore.RESET)

            try_time = 0
            message_sent = utils.send_message(number, message, sleepTime, img_path, pdf_path, driver)

            if message_sent == True:
                print("Message sent for number "+ Fore.GREEN + number + Fore.RESET + " is true")
                
                cursor.execute(f"SELECT * FROM goals WHERE name = 'sent done'")
                sent_goal = int(cursor.fetchall()[0][2]) + 1
                cursor.execute(f"SELECT * FROM goals WHERE name = 'all done'")
                all_goal = int(cursor.fetchall()[0][2]) + 1

                cursor.execute(f"UPDATE messages SET stats = 'sent' WHERE id = {id}")
                cursor.execute(f"UPDATE goals SET goal={sent_goal} WHERE name = 'sent done'")
                cursor.execute(f"UPDATE goals SET goal={all_goal} WHERE name = 'all done'")

                mydb.commit()
                break

            elif try_time == int(tryTime):
                print("Message sent for number " + Fore.RED + number + Fore.RESET + " is skipped")

                cursor.execute(f"SELECT * FROM goals WHERE name = 'sent done'")
                sent_goal = int(cursor.fetchall()[0][2]) + 1
                cursor.execute(f"SELECT * FROM goals WHERE name = 'all done'")
                all_goal = int(cursor.fetchall()[0][2]) + 1

                cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
                cursor.execute(f"UPDATE goals SET goal={sent_goal} WHERE name = 'sent done'")
                cursor.execute(f"UPDATE goals SET goal={all_goal} WHERE name = 'all done'")

                mydb.commit()
                break

            elif message_sent == 'not defined':
                print("Account for number " + Fore.RED + number + Fore.RESET + " is not defined")
                try_time += 1
                time.sleep(5)

            elif message_sent == 'cant send':
                print("Account for number " + Fore.RED + number + Fore.RESET + " is not loaded")
                try_time += 1
                time.sleep(30)

            elif message_sent == False:
                print("Account for number " + Fore.RED + number + Fore.RESET + " is invalid")

                cursor.execute(f"SELECT * FROM goals WHERE name = 'sent done'")
                sent_goal = int(cursor.fetchall()[0][2]) + 1
                cursor.execute(f"SELECT * FROM goals WHERE name = 'all done'")
                all_goal = int(cursor.fetchall()[0][2]) + 1
                
                cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
                cursor.execute(f"UPDATE goals SET goal={sent_goal} WHERE name = 'sent done'")
                cursor.execute(f"UPDATE goals SET goal={all_goal} WHERE name = 'all done'")

                mydb.commit()
                break

    cursor.execute(f"UPDATE settings SET value = 'No' WHERE name = 'av-checking'")
    mydb.commit()

input("Enter to start")
while True:
    check_db()
    time.sleep(60)