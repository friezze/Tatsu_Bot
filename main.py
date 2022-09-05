import logging
import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types


#bot = Bot('1783221355:AAG67NX3PHUkbD1HGICs2JK4kEh4i93xv7I') #<------------ Токен твоего бота хуярить сюда
#берётся у @BotFather


 #время --> указывается в секундах, а не в милисекундах, как в Срр

my_id = '644914405'

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("нет ты, " + message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

#time.sleep(N*10)

#bot.send_message(my_id, "СУКА БЛЯ")

#subprocess.Popen(["cmd.exe".encode('UTF8')], encoding='cp866')





#cmd = "date"

# returns output as byte string
#returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
#print('Current date is:', returned_output.decode("utf-8"))

