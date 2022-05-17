import utils, sys, mysql.connector, time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "shayanwilliams",
    database = "pishtazan"
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

        cursor.execute("SELECT * FROM settings WHERE name = 'sleep time'")
        sleepTime = cursor.fetchall()[0][2]

        if not res[0]:
            break

        for x in res:
            id, number, message, stats, activity_time = x
            message_sent = utils.send_message(number, message, sleepTime, driver)
            if message_sent:
                cursor.execute(f"UPDATE messages SET stats = 'sent' WHERE id = {id}")
                mydb.commit()
            else:
                cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
                mydb.commit()

    cursor.execute(f"UPDATE settings SET value = 'No' WHERE name = 'av-checking'")
    mydb.commit()

input("Enter to start")
while True:
    check_db()
    time.sleep(60)