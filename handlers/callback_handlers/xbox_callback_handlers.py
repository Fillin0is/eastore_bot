from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.filters import StateFilter, Command
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_GAME_RU
from services.services import get_rate_turkey
from keyboards.keyboards import inline_keyboard_regions_xbox, inline_keyboard_calculate_xbox_turkey,  inline_keyboard_functions_xbox_turkey, inline_keyboard_main

router = Router(name=__name__)

error_emojis = ['😕', '😞', '😟', '🙁', '😢', '😭', '😓', '😔', '😖', '😣']

class PriceTurkeyCalcXbox(StatesGroup):
    amount = State()

class PriceSentTurkeyXbox(StatesGroup):
    amount = State()


# -----------------------------------------------------------------------------
# --------------------------MicrosoftStore (Xbox)------------------------------

# Меню после выбора платформы Xbox
try:
    @router.callback_query(F.data.in_(['xbox_pressed', 'exit_region_xbox_pressed']))
    async def show_xbox_regions(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/xbox_region_photo.PNG'
                ),  # Используйте InputMediaPhoto
                caption='Выберите регион:',
            ),
            reply_markup=inline_keyboard_regions_xbox
        )
        await callback_query.answer()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Меню функицй региона Турции Microsoft Store (Xbox)
try:
    @router.callback_query(F.data.in_(['turkey_xbox_pressed', 'exit_function_xbox_turkey_pressed']))
    async def show_turkey_xbox_functions(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/xbox_turkey.jpg'
                ), 
                caption='Выберите категорию:',
            ),
            reply_markup=inline_keyboard_functions_xbox_turkey
        )
        await callback_query.answer()
        await state.clear()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Меню калькулятора Турецкого региона MS store
try:
    @router.callback_query(F.data == 'turkey_xbox_calculator_pressed')
    async def show_calculator_turkey_xbox(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/turkey_exchange_rate_xbox.jpg'
                ),
                caption='Введите стоимость товара в лирах (TL)',
            ),
            reply_markup=inline_keyboard_calculate_xbox_turkey
        )
        await state.set_state(PriceTurkeyCalcXbox.amount)
        await callback_query.answer()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Меню калькулятора Турции (MS store), реакция на неправиьные сообщения
try:
    @router.message(StateFilter(PriceTurkeyCalcXbox.amount))
    async def xbox_turkey_calculate(message: Message, bot: Bot, state: FSMContext):
        data = await state.get_data()
        
        if "message_id_calc" not in data.keys():
            message_id_calc = message.message_id - 1
            await state.update_data(message_id_calc=message_id_calc)
        else:
            message_id_calc = data["message_id_calc"]

        # Получаем текущий индекс эмодзи или начинаем с 0
        emoji_index = data.get("emoji_index", 0)

        # Проверяем, является ли текст числом и больше ли он нуля
        if message.text.isdigit() and int(message.text) > 0 and message.text[0] != '0':
            amount = float(message.text)
            try:
                await bot.edit_message_media(
                    chat_id=message.chat.id,
                    message_id=message_id_calc,
                    media=InputMediaPhoto(
                        media=FSInputFile(
                            path='photo/turkey_exchange_rate_xbox.jpg'
                        ),
                        caption=f'Сумма заказа к оплате = {get_rate_turkey(amount)} (₽)\n\nВведите стоимость товара в лирах (TL)',
                    ),
                    reply_markup=inline_keyboard_calculate_xbox_turkey
                )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except Exception as e:
                await bot.edit_message_media(
                        chat_id=message.chat.id,
                        message_id=message_id_calc,
                        media=InputMediaPhoto(
                            media=FSInputFile(
                                path='photo/turkey_exchange_rate_xbox.jpg'
                            ),
                            caption=f'Сумма заказa к оплaте = {get_rate_turkey(amount)} (₽)\n\nВведите стоимость товара в лирах (TL)',
                        ),
                        reply_markup=inline_keyboard_calculate_xbox_turkey
                    )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        else:
            # Выбираем эмодзи и обновляем индекс
            current_emoji = error_emojis[emoji_index]
            emoji_index = (emoji_index + 1) % len(error_emojis)
            await state.update_data(emoji_index=emoji_index)

            # Удаляем текущее сообщение с неправильным вводом
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            
            # Отправляем сообщение с ошибкой и эмодзи
            await bot.edit_message_media(
                chat_id=message.chat.id,
                message_id=message_id_calc,
                media=InputMediaPhoto(
                    media=FSInputFile(
                        path='photo/turkey_exchange_rate_xbox.jpg'
                    ),
                    caption=f'Некорректно введена стоимость товара {current_emoji}\n\nВведите стоимость товара в лирах (TL)',
                ),
                reply_markup=inline_keyboard_calculate_xbox_turkey
            )
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()

    
# Топ игр в турецком регионе MS store
try:
    @router.callback_query(F.data == 'turkey_buy_xbox_pressed')
    async def show_game_xbox_turkey(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/xbox_indiana_jones.jpg'
                ), 
                caption=LEXICON_GAME_RU['game_xbox_turkey']
            ),
            reply_markup=inline_keyboard_calculate_xbox_turkey
        )
        await callback_query.answer()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Подписки Xbox GamePass Ultimate турецком регионе MS store
try:
    @router.callback_query(F.data == 'turkey_xbox_sub_pressed')
    async def show_sub_xbox_turkey(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/gamepass_ultimate.jpg'
                ), 
                caption=LEXICON_RU['price_gamepass']
            ),
            reply_markup=inline_keyboard_calculate_xbox_turkey
        )
        await callback_query.answer()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Меню пополнения Турецкого региона MS store
try:
    @router.callback_query(F.data == 'turkey_xbox_sent_money_pressed')
    async def show_sent_money_turkey_xbox(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/sent_money.jpg'
                ),
                caption='Введите желаемое количество на пополнение в лирах (TL)',
            ),
            reply_markup=inline_keyboard_calculate_xbox_turkey
        )
        await state.set_state(PriceSentTurkeyXbox.amount)
        await callback_query.answer()
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()


# Меню пополнения Турции (MS store), реакция на неправиьные сообщения
try:
    @router.message(StateFilter(PriceSentTurkeyXbox.amount))
    async def xbox_turkey_sent_money(message: Message, bot: Bot, state: FSMContext):
        data = await state.get_data()
        
        if "message_id_calc" not in data.keys():
            message_id_calc = message.message_id - 1
            await state.update_data(message_id_calc=message_id_calc)
        else:
            message_id_calc = data["message_id_calc"]

        # Получаем текущий индекс эмодзи или начинаем с 0
        emoji_index = data.get("emoji_index", 0)

        # Проверяем, является ли текст числом и больше ли он нуля
        if message.text.isdigit() and int(message.text) > 0 and message.text[0] != '0':
            amount = float(message.text)
            try:
                await bot.edit_message_media(
                    chat_id=message.chat.id,
                    message_id=message_id_calc,
                    media=InputMediaPhoto(
                        media=FSInputFile(
                            path='photo/sent_money.jpg'
                        ),
                        caption=f'Сумма на пополнение = {get_rate_turkey(amount)} (₽)\n\nВведите желаемое количество на пополнение в лирах (TL)',
                    ),
                    reply_markup=inline_keyboard_calculate_xbox_turkey
                )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except Exception as e:
                await bot.edit_message_media(
                        chat_id=message.chat.id,
                        message_id=message_id_calc,
                        media=InputMediaPhoto(
                            media=FSInputFile(
                                path='photo/sent_money.jpg'
                            ),
                            caption=f'Сумма нa пополнение = {get_rate_turkey(amount)} (₽)\n\nВведите желаемое количество на пополнение в лирах (TL)',
                        ),
                        reply_markup=inline_keyboard_calculate_xbox_turkey
                    )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        else:
            # Выбираем эмодзи и обновляем индекс
            current_emoji = error_emojis[emoji_index]
            emoji_index = (emoji_index + 1) % len(error_emojis)
            await state.update_data(emoji_index=emoji_index)

            # Удаляем текущее сообщение с неправильным вводом
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            
            # Отправляем сообщение с ошибкой и эмодзи
            await bot.edit_message_media(
                chat_id=message.chat.id,
                message_id=message_id_calc,
                media=InputMediaPhoto(
                    media=FSInputFile(
                        path='photo/sent_money.jpg'
                    ),
                    caption=f'Некорректно введено числовое значение на пополнение {current_emoji}\n\nВведите желаемое количество на пополнение в лирах (TL)',
                ),
                reply_markup=inline_keyboard_calculate_xbox_turkey
            )
except Exception as e:
    @router.message(Command(commands='start'))
    async def process_start_command(message: Message, state: FSMContext):
        file_path = 'photo/store.jpg'
        await message.bot.send_photo(
            chat_id=message.chat.id,
            photo=FSInputFile(
                path=file_path
            ),
            caption=LEXICON_RU['/start'],
            reply_markup=inline_keyboard_main
        )
        await state.clear()