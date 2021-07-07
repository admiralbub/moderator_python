from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN
import re
from sqllite import BD


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#banned_users = set()

@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
	await message.delete()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['ban'], user_id=464391445) # здесь укажи свой ID
async def handle_ban_command(message: types.Message):
	abuser_id = int(message.reply_to_message.from_user.id)
	
	bd = BD()
	if (not bd.ban_users(abuser_id)):
		bd.new_ban_users(abuser_id)

	await message.reply(f"Пользователь {abuser_id} заблокирован.")


@dp.message_handler()
async def delete_message(message: types.Message):
	abuser_id = int(message.from_user.id)
	bd = BD()
	if (bd.ban_users(abuser_id)):
		await message.delete()
	bad_word = ["Плохое слово","Дурак","Лох","Вау"]
	string_word = message.text
	if re.compile('|'.join(bad_word),re.IGNORECASE).search(string_word):
		await message.delete()

		#await message.reply("В чате запрещено писать плохие слова!")


if __name__ == '__main__':
	executor.start_polling(dp)