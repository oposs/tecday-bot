#!/usr/bin/env python
import os
from uuid import uuid4
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.environ['TELEGRAM_API_TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

SHORTGAME_NAME = 'game1'
BASE_URL = 'https://tecdays0.oetiker.ch/public/snake.html'


@dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == SHORTGAME_NAME)
async def send_game(callback_query: types.CallbackQuery):
    uid = str(callback_query.from_user.id)
    if callback_query.message:
        mid = str(callback_query.message)
        cid = str(callback_query.id)
        url = "{}?uid={}&mid={}&cid={}".format(BASE_URL, uid, mid, cid)
    else:
        imid = callback_query.inline_message_id
        url = "{}?uid={}&imid={}".format(BASE_URL, uid, imid)
    await bot.answer_callback_query(callback_query.id, url=url)


@dp.inline_handler()
async def send_game(inline_query: types.InlineQuery):
    await bot.answer_inline_query(inline_query.id,
                                  [types.InlineQueryResultGame(id=str(uuid4()),
                                                               game_short_name=SHORTGAME_NAME)])


# this is the last line
executor.start_polling(dp)
