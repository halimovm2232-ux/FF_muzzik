import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

WELCOME_TEXT = """🌐 Global Service аз MUZIK :

💬 Чати Асосӣ - @chatik_muzik
🤖 Пост Бот - @muzik_danat_bot
💲 Донат / Размен - @muzik_danat_bot
🏬 Канали Постҳо - @ff_muzik
👥 Информация - @muzik_ejje
🔗 Сеткаи Чатҳо - @chatik_muzik
✈️ Donate / Алмаз - @muzik_danat_bot

➖➖➖➖➖➖➖➖➖➖

👋 Салом! Ман MUZIK 🎵
- Шахси боэътимод, ки дар соҳаи Гарант кор мекунад
- Беш аз 60+ отзывы мусбат дорем ⭐
- Таҷрибаи зиёд дар муомилаҳои бехатар 🔐

🤝 Бо ҳама самтҳо кор мекунам:
- Донат / Алмаз / UC / Пули бозӣ
- Фурӯш ва харидани аккаунтҳо
- Ивазкунии ҳама гуна душворӣ
- Хизматрасониҳо ва молҳои рақамӣ

[ 👤 Юзерам як бор ва абадӣ @muzik_ejje ]"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💚 Пункти Хизматрасонӣ", url="https://t.me/chatik_muzik"),
         InlineKeyboardButton("💬 Отзывы", url="https://t.me/otzivi_muzik")],
        [InlineKeyboardButton("📢 Канал", url="https://t.me/ff_muzik"),
         InlineKeyboardButton("💬 ЧАТ", url="https://t.me/chatik_muzik")],
        [InlineKeyboardButton("💎 Алмаз Харидан", url="https://t.me/muzik_danat_bot")],
        [InlineKeyboardButton("🛡️ Гарант", url="https://t.me/muzik_ejje")],
    ]
    await update.message.reply_text(WELCOME_TEXT, reply_markup=InlineKeyboardMarkup(keyboard))

# --- Барои 24 соат зинда мондан дар Render ---
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "MUZIK Bot is Alive! ✅"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

def main():
    if not TOKEN:
        print("❌ Хатогӣ: BOT_TOKEN ёфт нашуд!")
        return
    
    # Flask-ро дар фони паси кор дарорем
    threading.Thread(target=run_flask, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот кор кард... ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
