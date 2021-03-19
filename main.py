import logging
import telegram
from telegram.ext import Updater, CommandHandler

import random

logging.basicConfig(
    level = logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

token = '1739361747:AAEYusGMDZB3JWW4GYE7MqdHjgc-8iYZV2A'

def start(update, context):
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversación")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} yo soy tu bot.")

def random_number(update, context):
    user_id = update.effective_user['id']
    logger.info(f"El usuario {user_id}, ha solicitado un número aleatorio")
    number = random.randint(0,1000)
    context.bot.sendMessage(chat_id=user_id, parse_mode="HTML", text=f"Número aleatorio: {number}")


if __name__ == "__main__":
    # Obtenemos informacion de nuestro bot
    my_bot = telegram.Bot(token=token)
    # print(my_bot.getMe())

    # Enlazamos nuestro updater con nuestro bot
    updater = Updater(my_bot.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Creamos los manejadores
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("random", random_number))

    # Start loop
    updater.start_polling()

    # Permite finalizar con Ctrl + C
    updater.idle()