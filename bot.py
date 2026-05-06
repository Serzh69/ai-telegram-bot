from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

TELEGRAM_TOKEN = "8755221835:AAGt_Pe2F7Kq2w45PFPqhFtgyjztgfZIA6s"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("💰 Ціна", callback_data="price")],
        [InlineKeyboardButton("📢 Facebook пост", callback_data="facebook")],
        [InlineKeyboardButton("ℹ️ Про бота", callback_data="about")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 Вітаю! Оберіть дію:",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "price":
        text = "💰 Наші ціни уточнюйте у менеджера."

    elif query.data == "facebook":
        text = "📢 Ось приклад Facebook поста:\n\n🔥 Нові товари вже в наявності!\nЗаходьте до нас сьогодні."

    elif query.data == "about":
        text = "🤖 Telegram bot на Python."

    else:
        text = "❓ Невідома команда."

    await query.edit_message_text(text)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text.lower()

    if "привіт" in user_message:
        reply = "👋 Привіт! Я Telegram bot."

    elif "хто ти" in user_message:
        reply = "🤖 Я AI assistant на Python."

    elif "facebook" in user_message:
        reply = "📢 Можу допомагати створювати пости для Facebook."

    elif "ціна" in user_message:
        reply = "💰 Ціну уточнюйте у менеджера."

    else:
        reply = f"🧠 Ви написали: {user_message}"

    await update.message.reply_text(reply)


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot is running...")

app.run_polling()