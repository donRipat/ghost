from aiogram import Bot, Dispatcher, F, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio
from main import *

API_TOKEN = '8148250977:AAGNk_oQ3J1GyA-rM9dx5A4kQfOqDaow4xc'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

class SomeStates(StatesGroup):
    get_name = State()
    confirmation = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Welcome to the game of GHOST 👻\nTell me your name:")
    await state.set_state(SomeStates.get_name)

@dp.message(SomeStates.get_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.update_data(current_string="")
    data = await state.get_data() 
    await message.answer(f"Good to know you, {data['name']}\nOur game begins!")
    start_game(message.text)
    await state.set_state(SomeStates.game)

@dp.message(SomeStates.game)
async def process_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Current string: _{data['current_string']}_\n"
    data = await state.get_data() 
    await message.answer(f"Good to know you, {data['name']}\nOur game begins!")
    start_game(message.text)
    await state.set_state(SomeStates.game)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
