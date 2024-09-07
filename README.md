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
