from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menyu"))

addresses_keyboard = ReplyKeyboardMarkup(resize_yboard=True)
addresses_keyboard.add(KeyboardButton("1"))
addresses_keyboard.add(KeyboardButton("2"))
addresses_keyboard.add(KeyboardButton("3"))
addresses_keyboard.add(KeyboardButton("4"))
addresses_keyboard.add(KeyboardButton("5"))
addresses_keyboard.add(KeyboardButton("6"))
addresses_keyboard.add(KeyboardButton("7"))
addresses_keyboard.add(KeyboardButton("Back"))