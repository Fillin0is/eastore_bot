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

tg_reviews_button = InlineKeyboardButton(
    text='Отзывы',
    url='https://t.me/eapsstore/76'
)

rows_info = [[tg_admin_button], [tg_channel_button], [tg_reviews_button]]

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

rows_main_menu = [[ps_button], [xbox_button], [steam_button], [tg_admin_button], [tg_reviews_button]]

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

turkey_game_ps_button = InlineKeyboardButton(
    text='Игры',
    callback_data='turkey_buy_pressed'
)

turkey_ps_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='turkey_ps_sub_pressed'
)

turkey_game_donation__button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='turkey_ps_donat_pressed'
)

turkey_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='turkey_sent_money_ps_pressed'
)

turkey_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='turkey_ps_calculator_pressed'
)

exit_ps_region_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_region_ps_pressed'
)

turkey_functions = [[turkey_game_ps_button, turkey_ps_sub_button], [turkey_money_button, turkey_game_donation__button], [turkey_calculator_button], [exit_ps_region_button]]

inline_keyboard_functions_ps_turkey = InlineKeyboardMarkup(inline_keyboard=turkey_functions)

# ------------------------------------------------



# ------------------------------------------------

exit_function_ps_turkey_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_ps_turkey_pressed'
)

calculation_ps_turkey = [[tg_admin_button], [exit_function_ps_turkey_button]]

inline_keyboard_calculate_ps_turkey = InlineKeyboardMarkup(inline_keyboard=calculation_ps_turkey)

# ----------------------------------------------

ukraine_ps_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='ukraine_buy_ps_pressed'
)

ukraine_ps_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='ukraine_ps_sub_pressed'
)

ukraine_ps_game_donation_button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='ukeaine_ps_game_donation_pressed'
)

ukraine_ps_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='ukraine_ps_sent_money_pressed'
)

ukraine_ps_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='ukraine_ps_calculator_pressed'
)

ukraine_ps_functions = [[ukraine_ps_game_button, ukraine_ps_sub_button], [ukraine_ps_game_donation_button, ukraine_ps_money_button], [ukraine_ps_calculator_button], [exit_ps_region_button]]

inline_keyboard_functions_ps_ukraine = InlineKeyboardMarkup(inline_keyboard=ukraine_ps_functions)

# ------------------------------------------------

exit_function_ps_ukraine_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_ps_ukraine_pressed'
)

calculation_ps_ukraine = [[tg_admin_button], [exit_function_ps_ukraine_button]]

inline_keyboard_calculate_ps_ukraine = InlineKeyboardMarkup(inline_keyboard=calculation_ps_ukraine)

# ----------------------------------------------

india_ps_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='india_buy_ps_pressed'
)

india_ps_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='india_ps_sub_pressed'
)

india_ps_game_donation_button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='india_ps_game_donation_pressed'
)

india_ps_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='india_ps_sent_money_pressed'
)

india_ps_functions = [[india_ps_game_button, india_ps_sub_button], [india_ps_game_donation_button, india_ps_money_button], [exit_ps_region_button]]

inline_keyboard_functions_ps_india = InlineKeyboardMarkup(inline_keyboard=india_ps_functions)

# ------------------------------------------------

exit_function_ps_india_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_ps_india_pressed'
)

calculation_ps_india = [[tg_admin_button], [exit_function_ps_india_button]]

inline_keyboard_exit_ps_india = InlineKeyboardMarkup(inline_keyboard=calculation_ps_india)

# ------------------------------------------------------------------------------------
# -----------------------------MicrosoftStore (Xbox)----------------------------------

turkey_xbox_button = InlineKeyboardButton(
    text='Турция',
    callback_data='turkey_xbox_pressed'
)

xbox_regions = [[turkey_xbox_button], [exit_button]]

inline_keyboard_regions_xbox = InlineKeyboardMarkup(inline_keyboard=xbox_regions)

#----------------Функции турецкого региона Microsoft Store (Xbox)------------

turkey_xbox_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='turkey_buy_xbox_pressed'
)

turkey_xbox_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='turkey_xbox_sub_pressed'
)

turkey_xbox_game_donation_button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='turkey_xbox_game_donation_pressed'
)

turkey_xbox_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='turkey_xbox_sent_money_pressed'
)

turkey_xbox_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='turkey_xbox_calculator_pressed'
)

exit_xbox_region_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_region_xbox_pressed'
)

turkey_xbox_functions = [[turkey_xbox_game_button, turkey_xbox_sub_button], [turkey_xbox_game_donation_button, turkey_xbox_money_button], [turkey_xbox_calculator_button], [exit_xbox_region_button]]

inline_keyboard_functions_xbox_turkey = InlineKeyboardMarkup(inline_keyboard=turkey_xbox_functions)

# ------------------------Калькулятор курса Microsoft Store (Турция)----------------

exit_function_xbox_turkey_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_xbox_turkey_pressed'
)

calculation_xbox_turkey = [[tg_admin_button], [exit_function_xbox_turkey_button]]

inline_keyboard_calculate_xbox_turkey = InlineKeyboardMarkup(inline_keyboard=calculation_xbox_turkey)


# -----------------------------------------------------------------------------------
# -------------------------------------Steam Казахстан (PC)------------------------------------

kazach_steam_button = InlineKeyboardButton(
    text='Казахстан',
    callback_data='kazah_steam_pressed'
)

ukraine_steam_button = InlineKeyboardButton(
    text='Украина',
    callback_data='ukraine_steam_pressed'
)

steam_regions = [[kazach_steam_button], [ukraine_steam_button], [exit_button]]

inline_keyboard_regions_steam = InlineKeyboardMarkup(inline_keyboard=steam_regions)

#----------------Функции Казахстанского региона Steam (PC)----------------------------

kazah_steam_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='kazah_buy_steam_pressed'
)

kazah_steam_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='kazah_steam_sub_pressed'
)

kazah_steam_game_donation_button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='kazah_steam_game_donation_pressed'
)

kazah_steam_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='kazah_steam_sent_money_pressed'
)

kazah_steam_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='kazah_steam_calculator_pressed'
)

exit_steam_region_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_region_steam_pressed'
)

kazah_steam_functions = [[kazah_steam_game_button, kazah_steam_sub_button], [kazah_steam_game_donation_button, kazah_steam_money_button], [kazah_steam_calculator_button], [exit_steam_region_button]]

inline_keyboard_functions_steam_kazah = InlineKeyboardMarkup(inline_keyboard=kazah_steam_functions)

# ------------------------Калькулятор курса Steam(Казахстан)--------------------------

exit_function_steam_kazah_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_steam_kazah_pressed'
)

calculation_steam_kazah = [[tg_admin_button], [exit_function_steam_kazah_button]]

inline_keyboard_calculate_steam_kazah = InlineKeyboardMarkup(inline_keyboard=calculation_steam_kazah)

# -----------------------------------------------------------------------------------
# -------------------------------------Steam Украина (PC)------------------------------------

#----------------Функции Казахстанского региона Steam (PC)----------------------------

ukraine_steam_game_button = InlineKeyboardButton(
    text='Игры',
    callback_data='ukraine_buy_steam_pressed'
)

ukraine_steam_sub_button = InlineKeyboardButton(
    text='Подписки',
    callback_data='ukraine_steam_sub_pressed'
)

ukraine_steam_game_donation_button = InlineKeyboardButton(
    text='Игровой донат',
    callback_data='ukraine_steam_game_donation_pressed'
)

ukraine_steam_money_button = InlineKeyboardButton(
    text='Пополнение кошелька',
    callback_data='ukraine_steam_sent_money_pressed'
)

ukraine_steam_calculator_button = InlineKeyboardButton(
    text='Калькулятор цен',
    callback_data='ukraine_steam_calculator_pressed'
)

ukraine_steam_functions = [[ukraine_steam_game_button, ukraine_steam_sub_button], [ukraine_steam_game_donation_button, ukraine_steam_money_button], [ukraine_steam_calculator_button], [exit_steam_region_button]]

inline_keyboard_functions_steam_ukraine = InlineKeyboardMarkup(inline_keyboard=ukraine_steam_functions)

# ------------------------Калькулятор курса Steam(Казахстан)--------------------------

exit_function_steam_ukraine_button = InlineKeyboardButton(
    text='<< Назад',
    callback_data='exit_function_steam_ukraine_pressed'
)

calculation_steam_ukraine = [[tg_admin_button], [exit_function_steam_ukraine_button]]

inline_keyboard_calculate_steam_ukraine = InlineKeyboardMarkup(inline_keyboard=calculation_steam_ukraine)