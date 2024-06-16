import logging
rom db  import Database
from button import menu_keyboard, addresses_keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6849879495:AAGf_ppbYBokJfhIdV-7z1yjmy9zwU29pL0'


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Sizni yana ko'rganimdan xursandman @{username}", reply_markkup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xush kelibsiz @{username}", reply_markup=menu_keyboard)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"Sizga qanday yordam beraolamiz @{username}")




@dp.message_handler(lambda message: message.text == "Menyu")
async def menu(message: types.Message):
    await message.answer("Menyular", reply_markup=addresses_keyboard)

@dp.message_handler(lambda message: message.text == "Back")
async def menu(message: types.Message):
    await message.answer("Back", reply_markup=menu_keyboard)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

