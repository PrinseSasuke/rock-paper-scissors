from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_start = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text = "Начать"),
            KeyboardButton(text = "Назад")
        ]
    ],
    resize_keyboard=True
)