from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnUrlChannel = InlineKeyboardButton(text='Subscribe ↗', url='https://t.me/bilol_works')
btnDoneSub = InlineKeyboardButton(text="Subscribed ✔", callback_data='subchanneldone')

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.add(btnUrlChannel, btnDoneSub)