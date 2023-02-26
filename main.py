from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import os
import datetime
from dotenv import load_dotenv

from for_requests import get_timetable, get_timetable_next_week
from for_parser import timetable_on_week, timetable_on_today, timetable_next_week, get_schedule_time


KEYBOARD_STANDARD = Keyboard(one_time=False, inline=False)\
    .add(Text("Сегодня"), color=KeyboardButtonColor.PRIMARY)\
    .row()\
    .add(Text("Неделя"), color=KeyboardButtonColor.PRIMARY)\
    .row()\
    .add(Text("Следующая неделя"), color=KeyboardButtonColor.PRIMARY)\
    .row()\
    .add(Text("Звонки"), color=KeyboardButtonColor.PRIMARY)

load_dotenv()
API_KEY = os.getenv('VK_API_KEY')


bot = Bot(token=API_KEY)
bot.labeler.vbml_ignore_case = True


@bot.on.private_message(text='Сегодня')
async def send_keyboard(message: Message):
    await message.answer(timetable_on_today(), keyboard=KEYBOARD_STANDARD)


@bot.on.private_message(text='Неделя')
async def send_keyboard(message: Message):
    await message.answer(timetable_on_week(), keyboard=KEYBOARD_STANDARD)


@bot.on.private_message(text='Следующая неделя')
async def send_keyboard(message: Message):
    await message.answer(timetable_next_week(), keyboard=KEYBOARD_STANDARD)


@bot.on.private_message(text='Звонки')
async def send_keyboard(message: Message):
    await message.answer(get_schedule_time(), keyboard=KEYBOARD_STANDARD)


@bot.loop_wrapper.interval(hours=1)
async def update():
    get_timetable()
    get_timetable_next_week()
    print('данные обновлены')


bot.run_forever()

