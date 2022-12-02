#!/usr/bin/env python3

import os
import random
from uuid import uuid4
from aiogram import Bot, Dispatcher, executor, types
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = 'MUSS-MIT-TOKEN-ERSETZT-WERDEN'
# SHORTGAME_NAME = 'game4'
# GAME_URL = 'https://tecdays0.oetiker.ch/public/X.html'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Dieser Code wird ausgeführt, sobald jemand im chat /start oder /help ein gibt
    :param message: eingegebene Chat Nachricht
    """
    await message.reply(f"Hallo *{message.from_user.first_name}* \n"
                        f"Ich bin der TecDays echo bot. \n"
                        f"Hinweis: Katzen sind _nicht_ mein Ding",
                        parse_mode='Markdown')


@dp.message_handler(regexp='(cat|katze|regen|chatz)')
async def send_cats(message: types.Message):
    """
    Dieser code wir ausgeführt, wenn in einer Nachricht an den Bot "cat", "katze" oder "regen" vorkommt
    :param message: eingegebene Chat Nachricht
    """

    # Wo sollen wir die Katzenbilder hernehmen
    cat_source_dir = 'public/cats'

    # Wir schauen welche Katzenbilder überhaupt vorhanden sind und speichern sie in der Variable "cats"
    cats = os.listdir(cat_source_dir)

    # Wir wählen zufällig eine Katze aus und speichern diese in der Variable "cat"
    cat = random.choice(cats)

    # Die Katze wird in den speicher geladen und in der Variable "photo" zwischen gespeichert
    with open(os.path.join(cat_source_dir, cat), 'rb') as photo:
        # Wir senden die ausgewählte Katze als Bild mit der Bildunterschrift welche unter anderem die eingegange
        # Nachricht enthält
        logging.info(f"Sende katze an: {message.from_user.first_name}")
        await message.reply_photo(photo, caption=f'Ich habe *{message.text}* gehört', parse_mode='Markdown')


@dp.message_handler()
async def send_echo(message: types.Message):
    """
    Dieser Code wird bei jeder eingehenden Nachricht ausgeführt und macht nichts anderes als die erhaltene Nachricht
    zurückzusenden
    :param message: eingegebene Chat Nachricht
    """
    logging.info(f"Erhalten: {message.text} -> Antworte: {message.from_user.first_name}")
    await message.answer(message.text)


# # ## Der Folgende Codeteil wird benötigt für einen Gamebot
# @dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == SHORTGAME_NAME)
# async def send_game(callback_query: types.CallbackQuery):
#     uid = str(callback_query.from_user.id)
#     logging.info(f"Sende game an: {callback_query.from_user.first_name}")
#     if callback_query.message:
#         mid = str(callback_query.message)
#         cid = str(callback_query.id)
#         url = "{}?uid={}&mid={}&cid={}".format(GAME_URL, uid, mid, cid)
#     else:
#         imid = callback_query.inline_message_id
#         url = "{}?uid={}&imid={}".format(GAME_URL, uid, imid)
#     logging.info(f"Sent url: {url}")
#     await bot.answer_callback_query(callback_query.id, url=url)
# # #
# # #
# # @td_gamebot1_bot
# @dp.inline_handler()
# async def send_game(inline_query: types.InlineQuery):
#     logging.info(f"Inline Query von: {inline_query.from_user.first_name}")
#     await bot.answer_inline_query(inline_query.id,
#                                   [types.InlineQueryResultGame(id=str(uuid4()),
#                                                                game_short_name=SHORTGAME_NAME)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
