from aiogram import types

from loader import dp
from transliterate import to_cyrillic,to_latin


# Echo bot
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    matni = message.text
    if matni.isascii():
        javobi = to_cyrillic(matni)
    else:
        javobi = to_latin(matni)
    await message.answer(javobi)
