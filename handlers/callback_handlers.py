from aiogram import F, Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

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

