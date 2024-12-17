from typing import Final
from telegram import Update


TOKEN: Final = '7522950368:AAFhmUZAhZ9XCK_fJ_0leLSlee1IHqoi5TE'
BOT_USERNAME: Final ='@CodeWithAlazarBot'

async def Start_command (update : Update, context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text ('Hello, Welcome to upgrade your sikll!')


# Respond

def clint_respond (text: str) -> str:
  proccess: str = text.lower()

  if 'hello' in text:
    return 'Hey What can I help you!'
  
  if 'i love python' in text:
    return 'Subscribe me 🥺'