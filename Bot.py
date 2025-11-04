import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# It's best practice to store your token in an environment variable
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command. Sends an image and an invitation link.
    """
    # The URL of the image you provided
    image_url = "https://freeimage.host/i/KQQBOve"
    # The invitation link for people to join
    group_invite_link = "https://t.me/+__g33bhB5Z41MzM1"
    
    # Caption that will appear under the image. You can customize this text.
    caption_text = f"Welcome! 🎉 Join our community here: {group_invite_link}"
    
    # Send the image with the caption containing the link
    await update.message.reply_photo(photo=image_url, caption=caption_text)

def main():
    """Main function to run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add a handler for the /start command
    application.add_handler(CommandHandler("start", start))
    
    # Start the Bot using polling
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
