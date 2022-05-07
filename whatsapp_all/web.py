import utils, sys
from flask import Flask, request
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com")

@app.route("/api/v1/messages/send", methods=['POST'])
def send_message():
    data = request.form

    if not data['number'] or not data['message'] or not data['sleep_time']:
        return "Please provide all the required fields.\n\[Number, Message, Sleep_Time]"

    message_sent = utils.send_message(data['number'], data['message'], data['sleep_time'], driver)
    print(message_sent)
    if message_sent:
        return "Message sent successfully"
    return f"Can't send message to {data['number']}"