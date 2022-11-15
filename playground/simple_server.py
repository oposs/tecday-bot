from sanic import Sanic
from sanic.response import text

app = Sanic("TecDaysSimpleServer")

app.static('/public', './public')


@app.get("/")
async def say_hello(request):
    return text("Hello")
