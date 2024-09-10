from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import inline_keyboard_main
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message, state: FSMContext):
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