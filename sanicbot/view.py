from sanic import Blueprint, Request, response, exceptions
from aiogram import Bot
from aiogram.types import Update
from sanic.log import logger
from aiogram.utils.exceptions import BadRequest

from .bot import get_bot, get_dp

bp = Blueprint("bot")


# register route to receive webhook update.
@bp.post("/bot/<token:str>")
async def on_webhook(request: Request, token: str):
    # get bot from app.ctx & get token from app.config
    bot = get_bot()
    dp = get_dp()

    # check the message is from telegram
    if token != bot._token:
        return response.empty(200)

    # set default instance.
    Bot.set_current(bot)
    update = Update(**request.json)

    # dispatch update message
    await dp.process_update(update)

    # must return status code 200.
    return response.empty(200)


@bp.get("/me")
async def me(request: Request):
    bot = get_bot()
    me_info = await bot.get_me()
    return response.json(me_info.to_python())


@bp.route("/setScore")
async def set_score(request: Request):
    bot = get_bot()
    user_id = request.args.get('uid')
    score = request.args.get('score', default='0')  # type: str
    inline_message_id = request.args.get('imid', None)
    message_id = request.args.get('mid', None)
    chat_id = request.args.get('cid', None)
    if score.isnumeric() and int(score) > 0:
        try:
            await bot.set_game_score(
                user_id=user_id,
                score=int(score),
                inline_message_id=inline_message_id,
                message_id=message_id,
                chat_id=chat_id
            )
        except BadRequest as e:
            logger.info(f'BadRequest: {e}')
            return response.empty(status=500)
    return response.empty(status=201)
