import logging
from engine import get_random_quote
from aiogram import Bot, Dispatcher, executor, types
import inlinekeyboard as nav

API_TOKEN = '2110525231:AAEhco9FpSpUCD7PrVPBE7N0NWDoKPcjaiI'
CHAT_ID = '@bilol_works'
NOT_SUB_MESSAGE = 'For using this bot please subscribe to my channel: @bilol_works\n' \
                  'This bot was made by @dynamiebilol 💣'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHAT_ID, user_id= message.from_user.id)):
        await message.reply(f"Hi  {message.chat.first_name} .Send me /quote command to get a random quote from me! \n"
                            f"\nThis bot was made by @dynamiebilol 💣")
    else:
        await message.reply(NOT_SUB_MESSAGE, reply_markup=nav.checkSubMenu)

@dp.message_handler(commands=['quote'])
async def send_quote(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)):
        await message.reply(text=get_random_quote())
    else:
        await message.reply(NOT_SUB_MESSAGE, reply_markup=nav.checkSubMenu)


@dp.message_handler()
async def instruction(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)):
        if message.text == '/quote':
            await message.reply(text=get_random_quote())
        else:
            await message.reply("Send me /quote command to get a random quote from me! \n "
                                "\nThis bot was made by @dynamiebilol 💣")
    else:
        await message.reply(NOT_SUB_MESSAGE, reply_markup=nav.checkSubMenu)



@dp.callback_query_handler(text = 'subchanneldone')
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHAT_ID, user_id= message.from_user.id)):
        await message.reply(f"Hi  {message.chat.first_name} .Send me /quote command to get a random quote from me! \n"
                            f"\nThis bot was made by @dynamiebilol 💣")
    else:
        await message.reply(NOT_SUB_MESSAGE, reply_markup=nav.checkSubMenu)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)