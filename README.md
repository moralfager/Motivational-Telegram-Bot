# Motivational Telegram Bot

## Description
This project is a Telegram bot designed to inspire and motivate users with random motivational quotes and beautiful images. The bot can respond to various commands and interact with users by providing them with motivational quotes or random photos. The quotes are sourced from a predefined list, while the images are fetched from an external website.

## Features
- **/motivation** or **/motivate**: Sends a random motivational quote from a collection.
- **/photo**: Sends a random photo from a list of wisdom images.
- **/help** or **/start**: Greets the user and provides instructions on how to use the bot.
- **Default Response**: If the bot doesn't understand the command, it suggests using one of the available commands.

## How It Works
- **Quote Source**: The bot reads from a JSON file (`quotes.json`) which contains motivational quotes.
- **Image Source**: The bot scrapes motivational images from a website using `BeautifulSoup` and stores the image URLs.
- **Randomization**: Both quotes and images are chosen randomly when requested by the user.

## Dependencies
- `telebot` for interacting with the Telegram API.
- `requests` for fetching web content.
- `beautifulsoup4` for web scraping and extracting image URLs.
- `unittest` for testing the bot's functionality.

## Setup
1. Install required dependencies:
   ```bash
   pip install telebot requests beautifulsoup4
2. Set up your Telegram bot API token in the code:
   - Replace the placeholder API token in `main.py`:
     ```python
     API_TOKEN = 'your-telegram-bot-api-token'
     ```
   - You can obtain a token by talking to the [BotFather](https://t.me/BotFather) on Telegram.

3. Create the `quotes.json` file:
   - Add your motivational quotes to the `quotes.json` file in the following format:
     ```json
     [
       {
         "quoteText": "Your time is limited, don't waste it living someone else's life.",
         "quoteAuthor": "Steve Jobs"
       },
       {
         "quoteText": "The only way to do great work is to love what you do.",
         "quoteAuthor": "Steve Jobs"
       }
     ]
     ```

4. Start your bot:
   - Run the following command to start the bot:
     ```bash
     python main.py
     ```

Once the bot is running, it will listen for commands and respond with motivational quotes or random images based on user input. You can interact with the bot in Telegram by typing `/motivate`, `/photo`, or `/start`.
