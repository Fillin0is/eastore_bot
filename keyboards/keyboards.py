from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем inline клавиатуру -------

tg_admin_button = InlineKeyboardButton(
    text='Связаться с нами',
    url= 'https://t.me/eastore_adm'
)

tg_channel_button = InlineKeyboardButton(
    text='Наша группа',
    url='https://t.me/eapsstore'
)

rows_info = [[tg_admin_button], [tg_channel_button]]

inline_keyboard_info = InlineKeyboardMarkup(inline_keyboard=rows_info)

pressed_1 = 'Нажата_1'

ps_button = InlineKeyboardButton(
    text='PlayStation Store',
    callback_data=pressed_1
)

pressed_2 = 'Нажата_2'

xbox_button = InlineKeyboardButton(
    text='Microsoft Store (Xbox)',
    callback_data=pressed_2
)

pressed_3 = 'Нажата_3'

steam_button = InlineKeyboardButton(
    text='Steam',
    callback_data=pressed_3
)

rows_main_menu = [[ps_button], [xbox_button], [steam_button]]

inline_keyboard_main = InlineKeyboardMarkup(inline_keyboard=rows_main_menu)



