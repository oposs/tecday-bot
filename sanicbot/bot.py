from sanic import Sanic
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentTypes, Message
from uuid import uuid4
from sanic.log import logger

SERVICE_CODE = "bot"
DP_CODE = f"{SERVICE_CODE}_dp"


def get_bot() -> Bot:
    app = Sanic.get_app()
    return getattr(app.ctx, SERVICE_CODE)


def get_dp() -> Dispatcher:
    app = Sanic.get_app()
    return getattr(app.ctx, DP_CODE)


def register(app: Sanic):
    # get bot_token from app.config
    token = app.config["BOT_TOKEN"]
    app_url = app.config["APP_URL"]
    webhook_url = f"{app_url}/bot/{token}"

    # define instance
    bot = Bot(token)
    dp = Dispatcher(bot)

    # listen aiogram message event.
    @dp.message_handler(content_types=ContentTypes.ANY)
    async def on_message(message: Message):
        await message.reply("Hello " + message.text)

    @dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == app.config["SHORTGAME_NAME"])
    async def send_game(callback_query: types.CallbackQuery):
        user_id = str(callback_query.from_user.id)
        if callback_query.message:
            message_id = str(callback_query.message)
            chat_id = str(callback_query.id)
            url = "{}?uid={}&mid={}&cid={}".format(
                app.config["GAME_URL"], user_id, message_id, chat_id)
        else:
            imid = callback_query.inline_message_id
            url = "{}?uid={}&imid={}".format(app.config["GAME_URL"], user_id, imid)
        await bot.answer_callback_query(callback_query.id, url=url)
        logger.info("send_game {}".format(url))

    @dp.inline_handler()
    async def send_game(inline_query: types.InlineQuery):
        await bot.answer_inline_query(
            inline_query.id,
            [types.InlineQueryResultGame(
                id=str(uuid4()),
                game_short_name=app.config["SHORTGAME_NAME"])])
        logger.info("send_game inline")

    # set webhook url on startup

    @app.main_process_start
    async def startup(app: Sanic):
        # send request to telegram for change webhook.
        await bot.set_webhook(webhook_url)

    # delete webhook before stop.
    @app.before_server_stop
    async def dispose(app: Sanic):
        await bot.delete_webhook()

    # attach bot & dispatcher to app.ctx
    setattr(app.ctx, SERVICE_CODE, bot)
    setattr(app.ctx, DP_CODE, dp)
