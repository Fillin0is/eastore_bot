from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.filters import StateFilter, Command
from aiogram.types import Message


from lexicon.lexicon_ru import LEXICON_GAME_RU, LEXICON_RU
from services.services import get_rate_turkey, get_rate_ukraine
from keyboards.keyboards import inline_keyboard_regions_ps, inline_keyboard_functions_ps_turkey, inline_keyboard_main, inline_keyboard_calculate_ps_turkey, inline_keyboard_functions_ps_ukraine, inline_keyboard_calculate_ps_ukraine

router = Router(name=__name__)

error_emojis = ['😕', '😞', '😟', '🙁', '😢', '😭', '😓', '😔', '😖', '😣']

class PriceTurkeyCalcPS(StatesGroup):
    amount = State()

class PriceUkraineCalcPS(StatesGroup):
    amount = State()

class PriceTurkeySentPS(StatesGroup):
    amount = State()

class PriceUkraineSentPS(StatesGroup):
    amount = State()

# ---------------------Playstation Store-------------------------

# Меню выбора региона PlayStation Store
try:
    @router.callback_query(F.data == 'ps_pressed')
    async def show_ps_regions(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_region_photo.png'
                ),
                caption='Выберите регион:',
            ),
            reply_markup=inline_keyboard_regions_ps
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


# Меню выбора региона Турции на Playstation
try:
    @router.callback_query(F.data == 'turkey_ps_pressed')
    async def show_turkey_fanctions(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_turkey_flag.jpg'
                ), 
                caption='Выберите категорию:',
            ),
            reply_markup=inline_keyboard_functions_ps_turkey
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


# Меню топа игр Турции на Playstation
try:
    @router.callback_query(F.data == 'turkey_buy_pressed')
    async def show_game_top_turkey(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/fc25.jpg'
                ), 
                caption=LEXICON_GAME_RU['game_ps_turkey']
            ),
            reply_markup=inline_keyboard_calculate_ps_turkey
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


# Возврат в главное меню из выбора региона ps
try:
    @router.callback_query(F.data == 'exit_main_pressed')
    async def exit_to_main_menu(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/store.jpg'
                ),
                caption='Главное меню:',
            ),
            reply_markup=inline_keyboard_main
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


# Возврат в меню выбора региона PlayStation Store
try:
    @router.callback_query(F.data == 'exit_region_ps_pressed')
    async def exit_to_region_menu(callback_query: CallbackQuery):
        await callback_query.answer()
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_region_photo.png'
                ),
                caption='Выберите регион:',
            ),
            reply_markup=inline_keyboard_regions_ps
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


# Выход из калькулятора указать выше
try:
    @router.callback_query(F.data == 'turkey_ps_calculator_pressed')
    async def show_calculator_turkey_ps(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/turkey_exchange_rate.jpg'
                ),
                caption='Введите стоимость товара в лирах (TL)',
            ),
            reply_markup=inline_keyboard_calculate_ps_turkey
        )
        await state.set_state(PriceTurkeyCalcPS.amount)
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
    

# Возврат в меню выбора региона PlayStation Store
try:
    @router.callback_query(F.data == 'exit_function_ps_turkey_pressed')
    async def exit_to_fanctions_ps_turkey(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_turkey_flag.jpg'
                ), 
                caption='Выберите категорию:',
            ),
            reply_markup=inline_keyboard_functions_ps_turkey
        )
        await state.set_state(default_state)
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


# калькулятор региона Турции PS store
try:
    @router.message(StateFilter(PriceTurkeyCalcPS.amount))
    async def ps_turkey_calculate(message: Message, bot: Bot, state: FSMContext):
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
                            path='photo/turkey_exchange_rate.jpg'
                        ),
                        caption=f'Сумма заказа к оплате = {get_rate_turkey(amount)} (₽)\n\nВведите стоимость товара в лирах (TL)',
                    ),
                    reply_markup=inline_keyboard_calculate_ps_turkey
                )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except Exception as e:
                await bot.edit_message_media(
                    chat_id=message.chat.id,
                    message_id=message_id_calc,
                    media=InputMediaPhoto(
                        media=FSInputFile(
                            path='photo/turkey_exchange_rate.jpg'
                        ),
                        caption=f'Сумма заказa к оплaте = {get_rate_turkey(amount)} (₽)\n\nВведите стоимость товара в лирах (TL)',
                    ),
                    reply_markup=inline_keyboard_calculate_ps_turkey
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
                        path='photo/turkey_exchange_rate.jpg'
                    ),
                    caption=f'Некорректно введена стоимость товара {current_emoji}\n\nПовторно введите стоимость товара в лирах (TL)',
                ),
                reply_markup=inline_keyboard_calculate_ps_turkey
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


# PS store, подписки, турция
try:
    @router.callback_query(F.data == 'turkey_ps_sub_pressed')
    async def show_ps_sub(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_sub_turkey.jpg'
                ), 
                caption='',
            ),
            reply_markup=inline_keyboard_calculate_ps_turkey
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


# Меню пополнения Турецкого региона PS
try:
    @router.callback_query(F.data == 'turkey_sent_money_ps_pressed')
    async def show_sent_money_turkey_ps(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/sent_money.jpg'
                ),
                caption='Введите желаемое количество на пополнение в лирах (TL)',
            ),
            reply_markup=inline_keyboard_calculate_ps_turkey
        )
        await state.set_state(PriceTurkeySentPS.amount)
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


# Меню пополнения Турции (Steam), реакция на неправиьные сообщения
try:
    @router.message(StateFilter(PriceTurkeySentPS.amount))
    async def ps_turkey_sent_money(message: Message, bot: Bot, state: FSMContext):
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
                    reply_markup=inline_keyboard_calculate_ps_turkey
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
                        reply_markup=inline_keyboard_calculate_ps_turkey
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
                reply_markup=inline_keyboard_calculate_ps_turkey
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


# -----------------Украинский регион PlayStation----------------------------

# Меню выбора региона Украины на Playstation
try:
    @router.callback_query(F.data == 'ukraine_ps_pressed')
    async def show_ukraine_ps_fanctions(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_ukraine_flag.jpg'
                ), 
                caption='Выберите категорию:',
            ),
            reply_markup=inline_keyboard_functions_ps_ukraine
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


# Меню категорий украинского региона PlayStation
try:
    @router.callback_query(F.data.in_(['exit_function_ps_ukraine_pressed', 'exit_function_ps_ukraine_pressed']))
    async def exit_to_fanctions_ps_ukraine(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_ukraine_flag.jpg'
                ), 
                caption='Выберите категорию:',
            ),
            reply_markup=inline_keyboard_functions_ps_ukraine
        )
        await state.set_state(default_state)
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


# Меню калькулятора Турции PS store
try:
    @router.callback_query(F.data == 'ukraine_ps_calculator_pressed')
    async def show_calculator_ukraine_ps(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ukraine_exchange_rate.jpg'
                ),
                caption='Введите стоимость товара в гривнах (UAH)',
            ),
            reply_markup=inline_keyboard_calculate_ps_ukraine
        )
        await state.set_state(PriceUkraineCalcPS.amount)
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


# Изменненное состояние калькулятор Украинского PS store
try:
    @router.message(StateFilter(PriceUkraineCalcPS.amount))
    async def ps_ukraine_calculate(message: Message, bot: Bot, state: FSMContext):
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
                            path='photo/ukraine_exchange_rate.jpg'
                        ),
                        caption=f'Сумма заказа к оплате = {get_rate_ukraine(amount)} (₽)\n\nВведите стоимость товара в гривнах (UAH)',
                    ),
                    reply_markup=inline_keyboard_calculate_ps_ukraine
                )
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except Exception as e:
                await bot.edit_message_media(
                    chat_id=message.chat.id,
                    message_id=message_id_calc,
                    media=InputMediaPhoto(
                        media=FSInputFile(
                            path='photo/ukraine_exchange_rate.jpg'
                        ),
                        caption=f'Сумма заказa к оплaте = {get_rate_ukraine(amount)} (₽)\n\nВведите стоимость товара в гривнах (UAH)',
                    ),
                    reply_markup=inline_keyboard_calculate_ps_ukraine
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
                        path='photo/ukraine_exchange_rate.jpg'
                    ),
                    caption=f'Некорректно введена стоимость товара {current_emoji}\n\nПовторно введите стоимость товара в гривнах (UAH)',
                ),
                reply_markup=inline_keyboard_calculate_ps_ukraine
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


# Меню топа игр Украины на Playstation
try:
    @router.callback_query(F.data == 'ukraine_buy_ps_pressed')
    async def show_game_top_ukraine(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/fc25.jpg'
                ), 
                caption=LEXICON_GAME_RU['game_ps_ukraine']
            ),
            reply_markup=inline_keyboard_calculate_ps_ukraine
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


# Подписки игр Украины на Playstation
try:
    @router.callback_query(F.data == 'ukraine_ps_sub_pressed')
    async def show_sub_ukraine(callback_query: CallbackQuery):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/ps_sub_ukraine.jpg'
                ), 
                caption=''
            ),
            reply_markup=inline_keyboard_calculate_ps_ukraine
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


# Меню пополнения Украинского региона PS
try:
    @router.callback_query(F.data == 'ukraine_ps_sent_money_pressed')
    async def show_sent_money_ukraine_ps(callback_query: CallbackQuery, state: FSMContext):
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/sent_money.jpg'
                ),
                caption='Введите желаемое количество на пополнение в гривнах (UAH)',
            ),
            reply_markup=inline_keyboard_calculate_ps_ukraine
        )
        await state.set_state(PriceUkraineSentPS.amount)
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


# Меню пополнения Украины (PS), реакция на неправиьные сообщения
try:
    @router.message(StateFilter(PriceUkraineSentPS.amount))
    async def ps_ukraine_sent_money(message: Message, bot: Bot, state: FSMContext):
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
                        caption=f'Сумма на пополнение = {get_rate_ukraine(amount)} (₽)\n\nВведите желаемое количество на пополнение в гривнах (UAH)',
                    ),
                    reply_markup=inline_keyboard_calculate_ps_ukraine
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
                            caption=f'Сумма нa пополнение = {get_rate_ukraine(amount)} (₽)\n\nВведите желаемое количество на пополнение в гривнах (UAH)',
                        ),
                        reply_markup=inline_keyboard_calculate_ps_ukraine
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
                    caption=f'Некорректно введено числовое значение на пополнение {current_emoji}\n\nВведите желаемое количество на пополнение в гривнах (UAH)',
                ),
                reply_markup=inline_keyboard_calculate_ps_ukraine
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