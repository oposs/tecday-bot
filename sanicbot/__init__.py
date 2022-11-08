from sanic import Sanic
from os import path
from . import config, bot, view

# define sanic app & aiogram bot
app = Sanic(__name__)
app.update_config(config)
# serve static files
#app.static('/public', path.dirname(__file__) + '/../public')
app.static('/public', './public')

# register bot.
bot.register(app)

# register blueprint
app.blueprint(view.bp)