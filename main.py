import telebot
import requests
import json
import config

TELEGRAM_BOT_TOKEN = config.Test_Python
GIGACHAT_API_URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
GIGACHAT_ACCESS_TOKEN = config.access_token
GIGACHAT_MODEL = "GigaChat:latest"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def get_gigachat_response(prompt):
    headers = {
        "Authorization": f"Bearer {GIGACHAT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GIGACHAT_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "top_p": 0.9,
        "n": 1,
        "stream": False,
        "max_tokens": 800
    }
    try:
        response = requests.post(GIGACHAT_API_URL, headers=headers, json=data, timeout=60, verify=False)
        response.raise_for_status()
        json_response = response.json()
        if "choices" in json_response and len(json_response["choices"]) > 0:
            return json_response["choices"][0]["message"]["content"]
        else:
            return "Ошибка: Не удалось получить ответ от Gigachat. Проверьте структуру ответа."
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе к Gigachat API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка при разборе JSON ответа от Gigachat: {e} Response text: {response.text if 'response' in locals() else 'No response'}"
    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-помощник. Если нужно больше информации то напиши /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Опиши мне свою проблему/вопрос и я помогу тебе с ним")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    gigachat_prompt = (f'Пользователь пытается решить задачу: "{user_message}".' "Дай ответ на его вопрос.")
    gigachat_response = get_gigachat_response(gigachat_prompt)
    response_text = f"""Вот что мне удалось найти:{gigachat_response}"""
    
    bot.reply_to(message, response_text)

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Бот упал с ошибкой: {e}")
