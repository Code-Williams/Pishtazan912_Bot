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

print("Connected to DataBase") if mydb else print("Can't connect to DataBase")
    
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
utils.start_setup(driver)

def check_db():
    while True:
        cursor.execute("SELECT * FROM messages WHERE stats = 'pending' LIMIT 1")
        res = cursor.fetchall()

        if not res: break

        print("-"*30)

        while True:
            cursor.execute(f"UPDATE messages SET stats = 'sending' WHERE id={res[0][0]}")
            mydb.commit()

            cursor.execute("SELECT * FROM settings WHERE name = 'sleep time'")
            sleepTime = cursor.fetchall()[0][2]

            cursor.execute("SELECT * FROM settings WHERE name = 'try time'")
            tryTime = cursor.fetchall()[0][2]

            cursor.execute("SELECT * FROM settings WHERE name = 'message'")
            message = cursor.fetchall()[0][2]

            id, number, message2, stats, activity_time = res[0]

            print(f"Start sending {number}")

            message_sent = utils.send_message(number, message, sleepTime, driver)

            if message_sent == True:
                print(f"+ Message sent for number [ {number} ]")
                
                cursor.execute(f"SELECT * FROM goals WHERE name = 'sent done'")
                sent_goal = int(cursor.fetchall()[0][2]) + 1

                cursor.execute(f"SELECT * FROM goals WHERE name = 'all done'")
                all_goal = int(cursor.fetchall()[0][2]) + 1

                cursor.execute(f"UPDATE messages SET stats = 'sent' WHERE id = {id}")
                cursor.execute(f"UPDATE goals SET goal={sent_goal} WHERE name = 'sent done'")
                cursor.execute(f"UPDATE goals SET goal={all_goal} WHERE name = 'all done'")

                mydb.commit()
                break

            elif message_sent == False:
                print(f"Account for number {number} is invalid")

                cursor.execute(f"SELECT * FROM goals WHERE name = 'all done'")
                all_goal = int(cursor.fetchall()[0][2]) + 1
                
                cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
                cursor.execute(f"UPDATE goals SET goal={all_goal} WHERE name = 'all done'")

                mydb.commit()
                break

while True:
    check_db()
    time.sleep(60)