# Price Monitor

A Python bot that monitors product prices and sends alerts when prices drop.

## Features

- Monitor product prices automatically
- Save price history to CSV
- Send alerts through Telegram
- Check prices every 10 minutes

## Requirements

- Python 3.10+
- requests
- beautifulsoup4

## Installation

Install dependencies:

pip install -r requirements.txt

## Configuration

Open `telegram_bot.py` and insert your Telegram bot credentials:

TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

## Run the bot

python main.py

The bot will:
- Scrape product prices
- Save price history
- Send a Telegram alert when the price drops below the target value