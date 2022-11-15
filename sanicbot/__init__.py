import configparser
from sanic import Sanic
from os import path

from . import bot, view


# parse ini config
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini')

# define sanic app & aiogram bot
app = Sanic(__name__)
app.update_config(dict(config['DEFAULT']))

print(app.config)
# serve static files
# app.static('/public', path.dirname(__file__) + '/../public')
app.static('/public', './public')

# register bot.
bot.register(app)

# register blueprint
app.blueprint(view.bp)

