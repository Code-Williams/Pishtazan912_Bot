import utils, sys, mysql.connector
from flask import Flask, request
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

app = Flask(__name__)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com")

@app.route("/api/v1/messages/send", methods=['POST'])
def send_message():
    data = request.form

    if not data['number'] or not data['message'] or not data['sleep_time']:
        return "Please provide all the required fields.\n\[Number, Message, Sleep_Time]"

    message_sent = utils.send_message(data['number'], data['message'], data['sleep_time'], driver)
    if message_sent:
        return "Message sent successfully"
    return f"Can't send message to {data['number']}"

@app.route("/api/v1/checkdb", methods=['POST'])
def check_db():
    cursor.execute(f"UPdATE settings SET value = 'no' WHERE name = 'av-checking'")
    mydb.commit()

    cursor.execute("SELECT * FROM messages WHERE stats = 'pending'")
    res = cursor.fetchall()

    for x in res:
        id, number, message, stats = x
        message_sent = utils.send_message(number, message, "2", driver)
        if message_sent:
            cursor.execute(f"UPDATE messages SET stats = 'sent' WHERE id = {id}")
            mydb.commit()

        cursor.execute(f"UPDATE messages SET stats = 'skipped' WHERE id = {id}")
        mydb.commit()

    cursor.execute(f"UPDATE settings SET value = 'yes' WHERE name = 'av-checking'")
    mydb.commit()
    return 'Done'