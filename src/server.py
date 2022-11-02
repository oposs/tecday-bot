#!/usr/bin/env python
import os

from flask import Flask, send_from_directory, request, Response
from aiogram import Bot
from aiogram.utils.exceptions import BadRequest

TOKEN = os.environ['TELEGRAM_API_TOKEN']

app = Flask(__name__)
bot = Bot(token=TOKEN)


@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('../public', path)


@app.route("/setScore")
async def set_score():
    uid = request.args.get('uid')
    score = request.args.get('score', 0)
    imid = request.args.get('imid', None)
    mid = request.args.get('mid', None)
    cid = request.args.get('cid', None)
    try:
        if imid is not None:
            await bot.set_game_score(user_id=uid, score=score, inline_message_id=imid)
        else:
            await bot.set_game_score(user_id=uid, score=score, message_id=mid, chat_id=cid)
    except BadRequest as e:
        app.logger.info('BadRequest: {}'.format(e.text))
        return Response(status=304)
    return Response(status=200)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
