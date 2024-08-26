from aiogram import F, Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import FSMContext, State

from keyboards.keyboards import inline_keyboard_regions_ps, inline_keyboard_functions_ps_turkey, inline_keyboard_main, inline_keyboard_calculate_ps_turkey

router = Router(name=__name__)

# Меню после выбора платформы PlayStation
@router.callback_query(F.data == 'ps_pressed')
async def show_ps_regions(callback_query: CallbackQuery):
    await callback_query.answer()  # Обязательно отвечаем на колбэк
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/store.jpg'
            ),  # Используйте InputMediaPhoto
            caption='Выберите регион:',
        ),
        reply_markup=inline_keyboard_regions_ps
    )

# Меню выбора региона Турции на Playstation
@router.callback_query(F.data == 'turkey_ps_pressed')
async def show_turkey_fanctions(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/turkey_flag.jpg'
            ), 
            caption='Выберите категорию:',
        ),
        reply_markup=inline_keyboard_functions_ps_turkey
    )

# Возврат в главное меню из выбора региона ps
@router.callback_query(F.data == 'exit_main_pressed')
async def exit_to_main_menu(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/store.jpg'
            ),
            caption='Главное меню:',
        ),
        reply_markup=inline_keyboard_main
    )

# Возврат в меню выбора региона PlayStation Store
@router.callback_query(F.data == 'exit_region_ps_turkey_pressed')
async def exit_to_region_menu(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/store.jpg'
            ),
            caption='Выберите регион:',
        ),
        reply_markup=inline_keyboard_regions_ps
    )

# Определяем состояния
class Form(StatesGroup):
    waiting_for_price = State()

@router.callback_query(F.data == 'turkey_ps_calculator_pressed')
async def show_calculator_turkey_ps(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(
                path='photo/turkey_exchange_rate.jpg'
            ),
            caption='Введите стоимость продукта:',
        ),
        reply_markup=inline_keyboard_calculate_ps_turkey
    )
    
    # Переходим в состояние ожидания ввода цены
    await Form.waiting_for_price.set()

@router.message(StateFilter(Form.waiting_for_price))
async def process_price_input(message: Message, state: FSMContext):
    try:
        price = float(message.text)  # Пробуем преобразовать ввод в число
        if price > 0:
            doubled_price = price * 2  # Умножаем стоимость на 2
            
            # Отправляем новое сообщение с фотографией и умноженной стоимостью
            await message.answer_photo(
                photo=FSInputFile(path='photo/turkey_exchange_rate.jpg'),
                caption=f'Введенная стоимость: {price}\nУмноженная стоимость: {doubled_price}',
                reply_markup=inline_keyboard_calculate_ps_turkey
            )
            await state.finish()  # Завершаем состояние
        else:
            await message.answer('Пожалуйста, введите стоимость продукта, которая больше 0.')
    except ValueError:
        await message.answer('Некорректный ввод. Пожалуйста, введите число больше 0.')