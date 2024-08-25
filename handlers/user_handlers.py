from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

from keyboards.keyboards import inline_keyboard_info, inline_keyboard_main

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        markup=inline_keyboard_main
    )

    

# Этот хэндлер срабатывает на команду /info
@router.message(Command(commands='info'))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/info'],
        reply_markup=inline_keyboard_info
    )

