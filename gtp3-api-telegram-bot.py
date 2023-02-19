# Importing libraries for our project
import json
import requests
import openai
import time

# Insert your OpenAI API key here
openai.api_key = ""

# The name of the pre-trained OpenAI model
model_engine = "text-davinci-003"

# Telegram API endpoint for sending messages
telegram_url = "https://api.telegram.org/bot{}/sendMessage"

# Telegram API endpoint for getting updates
telegram_updates_url = "https://api.telegram.org/bot{}/getUpdates?offset={}"

# The Telegram API token for your bot
telegram_token = ""

# A list to store the context of the last 5 user questions
context = [""]
answers = ['']
offset = -1
last_question = ""
last_answer = ""
while True:
    time.sleep(1)
    # Get the Telegram updates
    updates = json.loads(requests.get(telegram_updates_url.format(telegram_token, offset)).text)["result"]

    # Iterate through the updates
    for update in updates:
        # Get the user's message
        message = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        print(chat_id,message)
        offset = update['update_id']+1
        # Get the chat ID of the user

        # Send the message and context to the pre-trained OpenAI model

        longcontext =''

        for i in range(len(context)):
            longcontext= longcontext+ ". User:  "+context[i]+'; You answered: '+answers[i]
        longcontext = (longcontext[:1000] + '..') if len(longcontext) > 1000 else longcontext
        # Below Text describe the whole point of your product in order to train the model and allow the bot to answer questions.
        sb_context = """Text describe the whole essence of your product.

User: {}

User: {}
You:
""" .format (last_question, message)
