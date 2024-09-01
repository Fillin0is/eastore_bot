from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from lexicon.lexicon_ru import LEXICON_RU

from keyboards.keyboards import inline_keyboard_info, inline_keyboard_main

router = Router()


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


# Этот хэндлер срабатывает на команду /info
@router.message(Command(commands='info'))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/info'],
        reply_markup=inline_keyboard_info
    )