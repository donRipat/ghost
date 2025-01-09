from aiogram import Bot, Dispatcher, F, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio
from config import Top_First_Letters, Top_Last_Letters
from main import *
import yaml

API_TOKEN = '8148250977:AAGOu--0LpEmaEM8wI8hqvhKL-SChMfbMPk'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

words = []
with open("src/resources/words_ge_4.txt", "r") as f:
    words = f.read().split()
with open('config.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

Top_First_Letters = {}
Top_Last_Letters = {}
with open(CONFIG["resources"]["top_first_letters"], "r") as file:
    Top_First_Letters: dict[str, float] = {}
    for line in file:
        key, value = line.split(":")
        Top_First_Letters[key] = float(value)

with open(CONFIG["resources"]["top_last_letters"], "r") as file:
    Top_Last_Letters: dict[str, float] = {}
    for line in file:
        key, value = line.split(":")
        Top_Last_Letters[key] = float(value)
    

def play(ss, words=words):
    candidates = [word for word in words if ss in word]
    if len(candidates) <= 0:
        return "!"
    for word in candidates:
        index = word.find(ss)
        if len(word) > index+len(ss) and ss + word[index+len(ss)] not in words:
            return f">{word[index+len(ss)]}"
        elif index != 0 and word[index-1] + ss not in words:
            return f"<{word[index-1]}"
    return bluff(ss)


def bluff(ss):
    if rd.choice([True, False]):
        neighbor_letter = ss[-1]
        move = ">"
        letter_weight = {k: v for k, v in Top_Last_Letters.items() if k != neighbor_letter}
    else:
        neighbor_letter = ss[0]
        move = "<"
        letter_weight = {k: v for k, v in Top_First_Letters.items() if k != neighbor_letter}
    population = list(letter_weight.keys())
    move += rd.choices(
        population=population,
        weights=list(letter_weight.values()),
        k=1
    )[0]
    return move


class SomeStates(StatesGroup):
    get_name = State()
    game = State()
    get_players_move = State()
    process_players_move = State()
    confirmation = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Welcome to the game of GHOST 👻\nTell me your name:")
    await state.update_data(current_string="")
    await state.set_state(SomeStates.get_name)


@dp.message(SomeStates.get_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(f"Good to know you, {data['name']}\nOur game begins!")
    await state.set_state(SomeStates.game)


@dp.message(SomeStates.game)
async def round_start(message: types.Message, state: FSMContext):
    data = await state.get_data() 
    if data['current_string'] in words:
        await game_results(message, state)
    await message.answer(f"Current string: _{data['current_string']}_\n")
    await message.answer("ur turn:")
    await state.set_state(SomeStates.get_players_move)


@dp.message(SomeStates.get_players_move)
async def get_players_move(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(current_string=message.text+data['current_string'])
    await state.set_state(SomeStates.game)


@dp.message(SomeStates.process_players_move)
async def process_players_move(message: types.Message, state: FSMContext):
    await state.set_state(SomeStates.game)


async def game_results(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"word is spelled: {data['current_string']}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

