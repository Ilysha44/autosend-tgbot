import telebot
import time

BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)

whitelist = []

@bot.message_handler(commands=['send'])
def send_message_n_times(message):
    user_id = str(message.from_user.id)

    if user_id not in whitelist:
        return

    try:
        
        parts = message.text.split(' ', 2)
        if len(parts) != 3:
            bot.reply_to(message, "WRONG! use /send <amount> <message>")
            return

        try:
            n = int(parts[1])
            if n <= 0:
                bot.reply_to(message, "Only positives")
                return
            
        except ValueError:
            bot.reply_to(message, "Amount must be an int")
            return

        text = parts[2]

        for i in range(n):
            bot.send_message(message.chat.id, text)
            time.sleep(0.1)

    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, f"There is an error: {e}")

if __name__ == '__main__':
    print("Bot is running!")
    bot.infinity_polling()
