from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji
kb_menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(emoji.emojize(":raised_back_of_hand:")),
            KeyboardButton(emoji.emojize(":victory_hand:")),
            KeyboardButton(emoji.emojize(":oncoming_fist:"))
        ]
    ],
    resize_keyboard=True
)