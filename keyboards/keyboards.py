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

#--------------------------------------------------------

ps_button = InlineKeyboardButton(
    text='PlayStation Store',
    callback_data='ps_pressed'
)

xbox_button = InlineKeyboardButton(
    text='Microsoft Store (Xbox)',
    callback_data='xbox_pressed'
)

steam_button = InlineKeyboardButton(
    text='Steam',
    callback_data='steam_pressed'
)

rows_main_menu = [[ps_button], [xbox_button], [steam_button]]

inline_keyboard_main = InlineKeyboardMarkup(inline_keyboard=rows_main_menu)

#-------------------------------------------------------

turkey_ps_button = InlineKeyboardButton(
    text='Турция',
    callback_data='turkey_ps_pressed'
)

ukraine_ps_button = InlineKeyboardButton(
    text='Украина',
    callback_data='ukraine_ps_pressed'
)

india_ps_button = InlineKeyboardButton(
    text='Индия',
    callback_data='india_ps_pressed'
)

exit_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_main_pressed'
)

ps_regions = [[turkey_ps_button], [ukraine_ps_button], [india_ps_button], [exit_button]]

inline_keyboard_regions_ps = InlineKeyboardMarkup(inline_keyboard=ps_regions)

#--------------------------------------------------------

turkey_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='turkey_buy_pressed'
)

turkey_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='turkey_calculator_pressed'
)

turkey_game_donation__button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='turkey_calculator_pressed'
)

turkey_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='turkey_sent_money_pressed'
)

turkey_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='turkey_ps_calculator_pressed'
)

exit_region_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_region_ps_turkey_pressed'
)

turkey_functions = [[turkey_game_button, turkey_sub_button], [turkey_money_button, turkey_game_donation__button], [turkey_calculator_button], [exit_region_button]]

inline_keyboard_functions_ps_turkey = InlineKeyboardMarkup(inline_keyboard=turkey_functions)

# ------------------------------------------------

exit_function_ps_menu_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_ps_turkey_pressed'
)

calculation_ps_turkey = [[tg_admin_button], [exit_function_ps_menu_button]]

inline_keyboard_calculate_ps_turkey = InlineKeyboardMarkup(inline_keyboard=calculation_ps_turkey)