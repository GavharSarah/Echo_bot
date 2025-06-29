# Echo_bot



Echo Bot is a simple Telegram bot built with Python and aiogram. It replies to every message with the same message—ideal for testing or learning.It also has startup and shutdown functions which lets user know  when  the bot  started working and what time stopped 

## Features
- Echoes text messages
- Keeps token secret using a `.env` file
- Built with aiogram

## Setup
1. Clone the repo:
   `git clone https://github.com/GavharSarah/Echo_bot.git && cd Echo_bot`
2. Create a `.env` file and add your token:
   `TELEGRAM_BOT_TOKEN=your-bot-token-here`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run the bot:
   `python main.py`

## Notes
- Requires Python 3.7+
- `.env` is already ignored via `.gitignore`
- Keep your token secret

## License
MIT

