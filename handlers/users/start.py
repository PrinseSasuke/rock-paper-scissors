from aiogram import types
from keyboard import kb_menu, kb_menu_mode, kb_start, kb_end
from loader import dp
from states import mode_state
from aiogram.dispatcher import FSMContext
import random
import emoji
from utils.db_api import quick_commands as commands
@dp.message_handler(text = '/start')
async def command_start(message = types.Message):
    await message.answer(f"Hello {message.from_user.full_name} \n"
                         , reply_markup= kb_start)
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            pass
    except:
        await commands.add_user(user_id=message.from_user.id,
                                username = message.from_user.username,
                                status = "active",
                                balance = 250)
    await mode_state.mode.set()
@dp.message_handler(state = mode_state.mode,text = ["Начать", "Ещё раз"])
async def start_game(message: types.Message, state:FSMContext):
    answer = message.text
    user = await commands.select_user(message.from_user.id)
    if user.balance >= 50:
        await message.answer(text=f"Твой баланс {user.balance} 💵\n" + "Сделай ход", reply_markup=kb_menu)
        await state.update_data(mode = answer, bot = 0, player = 0)
        await mode_state.in_game.set()
    else:
        await message.answer("Не хватает баланса")

@dp.message_handler(state = mode_state.in_game, text = [emoji.emojize(':raised_back_of_hand:'), emoji.emojize(':victory_hand:'), emoji.emojize(':oncoming_fist:')])
async def start_game(message: types.Message, state:FSMContext):
    user = await commands.select_user(message.from_user.id)
    data = await state.get_data()
    mas = [emoji.emojize(':raised_back_of_hand:'), emoji.emojize(':victory_hand:'), emoji.emojize(':oncoming_fist:')]
    run_bot = random.choice(mas)
    result = ""
    if message.text == emoji.emojize(':raised_back_of_hand:'):
            if run_bot == emoji.emojize(':raised_back_of_hand:'):
                result = "Ничья"
            if run_bot == emoji.emojize(':victory_hand:'):
                    result = "Проигрыш"
            if run_bot == emoji.emojize(':oncoming_fist:'):
                    result = "Выигрыш"

    if message.text == emoji.emojize(':victory_hand:'):
        if run_bot == emoji.emojize(':raised_back_of_hand:'):
            result = "Выигрыш"
        if run_bot == emoji.emojize(':victory_hand:'):
            result = "Ничья"
        if run_bot == emoji.emojize(':oncoming_fist:'):
            result = "Проигрыш"

    if message.text == emoji.emojize(':oncoming_fist:'):

        if run_bot == emoji.emojize(':raised_back_of_hand:'):
            result = "Проигрыш"
            await commands.update_user_balance(message.from_user.id, -50)
        if run_bot == emoji.emojize(':victory_hand:'):
            result = "Выигрыш"

        if run_bot == emoji.emojize(':oncoming_fist:'):
            result = "Ничья"
    if result == "Выигрыш":
        await commands.update_user_balance(message.from_user.id, 50)
    if result  == "Проигрыш":
        await commands.update_user_balance(message.from_user.id, -50)
    await message.answer(f"Ход компьютера:{run_bot}\n"+
                         f"Результат:{result}\n", reply_markup=kb_end)
    await mode_state.end_game.set()
@dp.message_handler(state = mode_state.end_game,text =  "Ещё раз")
async def start_game(message: types.Message, state:FSMContext):
    answer = message.text
    user = await commands.select_user(message.from_user.id)
    if user.balance >= 50:

        await message.answer(text=f"Твой баланс {user.balance} 💵\n" + "Начинаем", reply_markup=kb_menu)
        await state.update_data(mode = answer, bot = 0, player = 0)
        await mode_state.in_game.set()
    else:
        await message.answer("Не хватает баланса")
@dp.message_handler(state = mode_state.end_game,text =  "Закончить")
async def end_game(message: types.Message, state:FSMContext):
    await message.reply("Чтобы начать - напиши /start", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
@dp.message_handler(text =  "/top")
async def end_game(message: types.Message, state:FSMContext):
    top_mas = await commands.select_all_users()
    await message.answer("Топ пользователей: \n"+
                         f"@{top_mas[0][-1]}: {top_mas[1][-1]}\n"+
                         f"@{top_mas[0][-2]}: {top_mas[1][-2]}\n")
