# GigaChat Telegram Assistant 🤖

A small educational project written entirely in Python that integrates Sberbank's GigaChat AI model into a Telegram bot.

The project demonstrates how to connect a Telegram bot to an external AI service using HTTP requests and process responses in JSON format.

It was created for learning purposes and is intended primarily for beginners exploring Python and AI integration.

## ✨ Features

- Integration with the GigaChat AI API.
- Telegram bot with `/start` and `/help` commands.
- AI-generated responses to user messages.
- HTTP requests using the `requests` library.
- JSON response processing.
- Simple configuration through a separate `config.py` file.
- No database required.

## 🛠️ Technologies

- **Python** — core programming language.
- **pyTelegramBotAPI (`telebot`)** — Telegram bot functionality.
- **Requests** — HTTP communication with the GigaChat API.
- **JSON** — processing API responses using Python's built-in module.
- **GigaChat API** — AI-powered responses.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/H1yro/Gigachat-Assistant.git
```

Replace the placeholders with your repository URL and project directory name.

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
python -m pip install pyTelegramBotAPI requests
```

The `json` module is included in Python's standard library and does not need to be installed separately.

### 3. Configure API credentials

#### GigaChat API

Visit the official developer portal:

https://developers.sber.ru/portal/gigachat-and-api

Follow the official instructions to obtain the credentials required to access GigaChat.

#### Telegram Bot

Create a Telegram bot using [@BotFather](https://t.me/BotFather) and obtain its token.

#### Configuration

Open `config.py` and provide both credentials:

```python
access_token = "YOUR_GIGACHAT_ACCESS_TOKEN"
Test_Python = "YOUR_TELEGRAM_BOT_TOKEN"
```

Keep your actual credentials private. Never publish your API access token or Telegram bot token in a public repository.

### 4. Run the bot

Start the Python script containing the bot's main code:

```bash
python main.py
```

Replace `main.py` if your main script has a different filename.

Once configured correctly, the bot can receive messages through Telegram and request AI-generated responses from GigaChat.

## 📚 Project Purpose

This project was created to practice:

- Integrating external APIs into Python applications.
- Sending HTTP POST requests.
- Working with JSON data.
- Handling API responses and request errors.
- Connecting a Telegram bot to an AI model.
- Separating configuration from application logic.

## ⚠️ Disclaimer

This is an independent educational project. It is not an official Sberbank product and is not affiliated with or endorsed by Sberbank.

The project is intended for learning and experimentation, not for production use.
