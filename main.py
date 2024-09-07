import json
import random
import telebot
import requests
from bs4 import BeautifulSoup

API_TOKEN = '6475732823:AAFhvysw42VRLHV7n96cgWmVMTcO5f_2tic'
bot = telebot.TeleBot(API_TOKEN)
url = 'https://everydaypower.com/wisdom-quotes/'
WisdomQuotes = []
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_='wp-block-image size-full')
else:
    print("Error fetching the webpage")
for i in elements:
    soup = BeautifulSoup(str(i), 'html.parser')

    # Find the img tag
    img_tag = soup.find('img')

    # Extract the src attribute
    img_src = img_tag['src'] if img_tag else 'Image source not found'

    WisdomQuotes.append(img_src)

with open('quotes.json', 'r', encoding='latin1') as file:
    quotes = json.load(file)

# Function to handle the /help and /start commands
@bot.message_handler(commands=['motivation', 'motivate'])
def send_motivation(message):
    # Select a random quote
    quote = random.choice(quotes)
    message_text = f"{quote['quoteText']} - {quote['quoteAuthor']}"
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, '''
    /motivation or /motivate - Sends a random motivational quote from a predefined list.
/help or /start - Welcomes the user and instructs them to use /motivate for motivation.
/photo - Sends a random photo from the 'WisdomQuotes' list, which contains URLs to images sourced from a website.
For any other text message - The bot will respond with a default message, indicating that it didn't understand the input and suggesting to use /help, /start, or /motivate''')

def send_random_photo(message):
    if WisdomQuotes:
        random_url = random.choice(WisdomQuotes)
        bot.send_photo(chat_id=message.chat.id, photo=random_url)
    else:
        bot.send_message(chat_id=message.chat.id, text="No images available.")

# Assuming you have a handler for a command, e.g., /photo
@bot.message_handler(commands=['photo'])
def handle_photo_command(message):
    send_random_photo(message)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'I didnt understand you, please type /help /start or /motivate')


bot.infinity_polling()