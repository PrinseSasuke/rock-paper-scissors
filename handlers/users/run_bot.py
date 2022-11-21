"""from aiogram import types
from keyboard import kb_menu
from loader import dp
import emoji
import random
from keyboard import kb_end
from aiogram.dispatcher import FSMContext
from states import mode_state
player = 0
bot = 0
mode = 0
mode_game = 0
from states import mode_state



@dp.message_handler(text = ['1', '3', '5'])
async def command_start(message = types.Message):
    global mode, mode_game
    mode = int(message.text)
    mode_game = mode
    await message.answer("your run:", reply_markup=kb_menu)


@dp.message_handler(text = [emoji.emojize(':raised_back_of_hand:'), emoji.emojize(':victory_hand:'), emoji.emojize(':oncoming_fist:')])

async def command_run(message = types.Message):
    global bot, player
    global mode, mode_game

    mas = [emoji.emojize(':raised_back_of_hand:'),emoji.emojize(':victory_hand:'), emoji.emojize(':oncoming_fist:') ]
    run_bot = random.choice(mas)
    result = ""
    if mode:
        print(mode)
        if message.text == emoji.emojize(':raised_back_of_hand:'):
            await message.answer(f"Run of bot: {run_bot}")
            if run_bot == emoji.emojize(':raised_back_of_hand:'):
                    result = "Ничья"
            if run_bot == emoji.emojize(':victory_hand:'):
                result = "Проигрыш"
            if run_bot == emoji.emojize(':oncoming_fist:'):
                result = "Выигрыш"

        if message.text == emoji.emojize(':victory_hand:'):
            await message.answer(f"Run of bot: {run_bot}")
            if run_bot == emoji.emojize(':raised_back_of_hand:'):
                result = "Выигрыш"
            if run_bot == emoji.emojize(':victory_hand:'):
                result = "Ничья"
            if run_bot == emoji.emojize(':oncoming_fist:'):
                result = "Проигрыш"

        if message.text == emoji.emojize(':oncoming_fist:'):
            await message.answer(f"Run of bot: {run_bot}")
            if run_bot == emoji.emojize(':raised_back_of_hand:'):
                result = "Проигрыш"
            if run_bot == emoji.emojize(':victory_hand:'):
                result = "Выигрыш"
            if run_bot == emoji.emojize(':oncoming_fist:'):
                result = "Ничья"
        if result == "Ничья":
            bot += 1
            player += 1
        if result == "Выигрыш":
            player += 1
        if result == "Проигрыш":
            bot += 1
        mode -= 1
        await  message.answer(f"Bot: {bot} You: {player}")
        if bot == mode_game // 2 + 1 == player:
            await message.answer("ничья")
            mode = 0
            player = 0
            bot = 0
            await message.answer("Сыграть ещё раз?", reply_markup=kb_end)
        elif bot == mode_game // 2 + 1:
            await message.answer("Bot win")
            mode = 0
            player = 0
            bot = 0
            await message.answer("Сыграть ещё раз?", reply_markup=kb_end)
        elif player == mode_game // 2 + 1:
            await message.answer("player win")
            mode = 0
            player = 0
            bot = 0
            await message.answer("Сыграть ещё раз?", reply_markup=kb_end)
"""

