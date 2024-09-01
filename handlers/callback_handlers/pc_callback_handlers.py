from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.filters import StateFilter
from aiogram.types import Message

# from lexicon.lexicon_ru import LEXICON_GAME_RU
from services.services import get_rate_ukraine, get_rate_kazah
from keyboards.keyboards import inline_keyboard_regions_steam, inline_keyboard_functions_steam_kazah, inline_keyboard_calculate_steam_kazah, inline_keyboard_calculate_steam_ukraine, inline_keyboard_functions_steam_ukraine

router = Router(name=__name__)

error_emojis = ['😕', '😞', '😟', '🙁', '😢', '😭', '😓', '😔', '😖', '😣']

class PriceKazahSteam(StatesGroup):
    amount = State()

class PriceUkraineSteam(StatesGroup):
    amount = State()


# ----------------------------------------------------------------------------------------
# -------------------------------PC (steam Казахстан)-------------------------------------

# Меню после выбора платформы Steam
@router.callback_query(F.data.in_(['steam_pressed', 'exit_region_steam_pressed']))
async def show_steam_regions(callback_query: CallbackQuery):
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/steam_region_photo.png'
            ),  # Используйте InputMediaPhoto
            caption='Выберите регион:',
        ),
        reply_markup=inline_keyboard_regions_steam
    )
    await callback_query.answer()


# Меню функицй региона Казахстана Steam (PC)
@router.callback_query(F.data.in_(['kazah_steam_pressed', 'exit_function_steam_kazah_pressed']))
async def show_kazah_steam_functions(callback_query: CallbackQuery):
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/steam_kazah.jpg'
            ), 
            caption='Выберите категорию:',
        ),
        reply_markup=inline_keyboard_functions_steam_kazah
    )
    await callback_query.answer()

@router.callback_query(F.data == 'kazah_steam_calculator_pressed')
async def show_calculator_kazah_steam(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/kazah_steam_exchange_rate.jpg'
            ),
            caption='Введите стоимость товара в тенге (KZ)',
        ),
        reply_markup=inline_keyboard_calculate_steam_kazah
    )
    await state.set_state(PriceKazahSteam.amount)
    await callback_query.answer()


@router.message(StateFilter(PriceKazahSteam.amount))
async def steam_kazah_calculate(message: Message, bot: Bot, state: FSMContext):
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
        await bot.edit_message_media(
            chat_id=message.chat.id,
            message_id=message_id_calc,
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/kazah_steam_exchange_rate.jpg'
                ),
                caption=f'Сумма заказа к оплате = {get_rate_kazah(amount)} (₽)\n\nВведите стоимость товара в тенге (KZ)',
            ),
            reply_markup=inline_keyboard_calculate_steam_kazah
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
                    path='photo/kazah_steam_exchange_rate.jpg'
                ),
                caption=f'Некорректно введена стоимость товара {current_emoji}\n\nВведите стоимость товара в тенге (KZ)',
            ),
            reply_markup=inline_keyboard_calculate_steam_kazah
        )

# ----------------------------------------------------------------------------------------
# -------------------------------PC (steam Украина)---------------------------------------

# Меню функицй региона Казахстана Steam (PC)
@router.callback_query(F.data.in_(['ukraine_steam_pressed', 'exit_function_steam_ukraine_pressed']))
async def show_ukraine_steam_functions(callback_query: CallbackQuery):
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/steam_ukraine.jpg'
            ), 
            caption='Выберите категорию:',
        ),
        reply_markup=inline_keyboard_functions_steam_ukraine
    )
    await callback_query.answer()

@router.callback_query(F.data == 'ukraine_steam_calculator_pressed')
async def show_calculator_ukraine_steam(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/steam_ukraine_exchange_rate.jpg'
            ),
            caption='Введите стоимость товара в гривнах (UAH)',
        ),
        reply_markup=inline_keyboard_calculate_steam_ukraine
    )
    await state.set_state(PriceUkraineSteam.amount)
    await callback_query.answer()


@router.message(StateFilter(PriceUkraineSteam.amount))
async def steam_ukraine_calculate(message: Message, bot: Bot, state: FSMContext):
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
        await bot.edit_message_media(
            chat_id=message.chat.id,
            message_id=message_id_calc,
            media=InputMediaPhoto(
                media=FSInputFile(
                    path='photo/steam_ukraine_exchange_rate.jpg'
                ),
                caption=f'Сумма заказа к оплате = {get_rate_ukraine(amount)} (₽)\n\nВведите стоимость товара в гривнаях (UAH)',
            ),
            reply_markup=inline_keyboard_calculate_steam_ukraine
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
                    path='photo/steam_ukraine_exchange_rate.jpg'
                ),
                caption=f'Некорректно введена стоимость товара {current_emoji}\n\nВведите стоимость товара в гривнах (UAH)',
            ),
            reply_markup=inline_keyboard_calculate_steam_ukraine
        )