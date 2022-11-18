from sanic import Sanic
from sanic.log import logger
from sanic.response import text, empty
from aiogram import Bot
from aiogram.utils.exceptions import BadRequest

TOKEN = "5729980052:AAHRhXvlb0HqgLtSzp1ZEV4fp7HHPKxc3qc"

app = Sanic("TecDaysSimpleServer")
bot = Bot(token=TOKEN)

app.static('/public', './public')


@app.get("/")
async def say_hello(request):
    return text("Hello")


@app.get("/setScore")
async def set_score(request):
    user_id = request.args.get('uid')
    score = request.args.get('score', 0)
    inline_message_id = request.args.get('imid', None)
    message_id = request.args.get('mid', None)
    chat_id = request.args.get('cid', None)
    try:
        await bot.set_game_score(
            user_id=user_id,
            score=int(score),
            inline_message_id=inline_message_id,
            message_id=message_id,
            chat_id=chat_id
        )
        logger.info(f"Score updated {score}")
    except BadRequest as e:
        logger.info(f"Score unchanged {score}")
        return empty(status=304)
    return empty(status=200)

app.run(host="0.0.0.0", port=8080)
