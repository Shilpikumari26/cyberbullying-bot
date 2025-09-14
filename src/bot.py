from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from service import predict

TOKEN = "8450785442:AAHoq0MfOU81Ujsvt1m-VCXBwai7WkfpGAU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I am Cyberbullying Detection Bot.\nSend me a message, and I’ll classify it.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    result = predict(user_text)

    if result == "bullying":
        response = "⚠️ Bullying detected!"
    else:
        response = "✅ This message seems safe."

    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
