from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler
from src.config import global_config
from src.logger import logger
from src.filter import groups_filter, private_filter


async def on_group_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="喵")


async def on_private_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="喵")


if __name__ == "__main__":
    application = ApplicationBuilder().token(global_config.telegram_bot_token).build()

    group_message_handler = MessageHandler(groups_filter, on_group_message)
    private_message_handler = MessageHandler(private_filter, on_private_message)

    application.add_handler(group_message_handler)
    application.add_handler(private_message_handler)
    logger.info("Start Listening for messages...")
    application.run_polling()
