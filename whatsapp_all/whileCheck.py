import utils, sys, mysql.connector, time, config
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

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

            id, number, message, stats, activity_time = res[0]

            try_time = 0
            message_sent = utils.send_message(number, message, sleepTime, driver)

            if message_sent == True:
                cursor.execute(f"UPDATE messages SET stats = 'sent' WHERE id = {id}")
                mydb.commit()
                break

            elif try_time == int(tryTime):
                cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
                mydb.commit()
                break

            elif message_sent == 'not defined':
                try_time += 1
                time.sleep(5)

            elif message_sent == 'cant send':
                try_time += 1
                time.sleep(30)

    cursor.execute(f"UPDATE settings SET value = 'No' WHERE name = 'av-checking'")
    mydb.commit()

input("Enter to start")
while True:
    check_db()
    time.sleep(60)