from aiogram import types
from keyboard import kb_menu, kb_menu_mode
from loader import dp

mode = 0
@dp.message_handler(text = ['1', '2', '3'])
async def command_start(message = types.Message):
    global mode
    mode = int(message.text)
    await message.answer("your run:", reply_markup=kb_menu)



