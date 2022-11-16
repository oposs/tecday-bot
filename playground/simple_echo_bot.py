import os
import random
from uuid import uuid4
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'XXXX'
SHORTGAME_NAME = 'XXX'
GAME_URL = 'XXXX'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hallo *{message.from_user.first_name}* \n"
                        f"Ich bin der TecDays echo bot. \n"
                        f"Hinweis: Katzen sind _nicht_ mein Ding",
                        parse_mode='Markdown')


@dp.message_handler(regexp='(^cat[s]?$|katze)')
async def send_cats(message: types.Message):
    cat_source_dir = 'public/cats'
    cats = os.listdir(cat_source_dir)
    cat = random.choice(cats)
    with open(os.path.join(cat_source_dir, cat), 'rb') as photo:
        await message.reply_photo(photo, caption=f'Ich habe *{message.text}* gehört. Hier ist deine Katze',
                                  parse_mode='Markdown')


@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer(message.text)


@dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == SHORTGAME_NAME)
async def send_game(callback_query: types.CallbackQuery):
    uid = str(callback_query.from_user.id)
    if callback_query.message:
        mid = str(callback_query.message)
        cid = str(callback_query.id)
        url = "{}?uid={}&mid={}&cid={}".format(GAME_URL, uid, mid, cid)
    else:
        imid = callback_query.inline_message_id
        url = "{}?uid={}&imid={}".format(GAME_URL, uid, imid)
    await bot.answer_callback_query(callback_query.id, url=url)


@dp.inline_handler()
async def send_game(inline_query: types.InlineQuery):
    await bot.answer_inline_query(inline_query.id,
                                  [types.InlineQueryResultGame(id=str(uuid4()),
                                                               game_short_name=SHORTGAME_NAME)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
