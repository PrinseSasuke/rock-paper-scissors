from aiogram import types
from keyboard import kb_menu, kb_menu_mode
from loader import dp
import emoji
@dp.message_handler(text = 'Еще раз')
async def command_start(message = types.Message):
    await message.answer(f"Hello {message.from_user.full_name} \n"+
                         "Your mode:", reply_markup= kb_menu_mode)
@dp.message_handler(text = 'Всё')
async def command_start(message = types.Message):
    await message.answer("/start", reply_markup=types.ReplyKeyboardRemove())