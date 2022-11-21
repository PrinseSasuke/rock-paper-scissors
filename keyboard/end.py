from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji
kb_end = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton("Ещё раз"),
            KeyboardButton(emoji.emojize("Закончить"))
        ]
    ],
    resize_keyboard=True
)