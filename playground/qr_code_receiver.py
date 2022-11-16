from sanic import Sanic, Request, Websocket, text
from sanic_ext import render
import json

app = Sanic("TecDaysQRReceiver")
app.ctx.open_web_sockets = {}
app.ctx.current_counter = 0


@app.get("/qr/counter_inc")
async def inc_counter(request: Request):
    app.ctx.current_counter = app.ctx.current_counter + 1
    to_remove = []
    for ws in app.ctx.open_web_sockets.values():
        try:
            await ws.send(json.dumps({
                'counter': app.ctx.current_counter,
                'user-agent': request.headers.get('User-Agent'),
                'remote-ip': request.headers.get('X-Forwarded-For')
            }))
        except Exception:
            to_remove.append(ws)
    for ws in to_remove:
        del app.ctx.open_web_sockets[ws]
    return await render("counter_inc.html", context={'counter': app.ctx.current_counter - 1}, status=200)


@app.get("/qr/counter_reset")
async def reset_counter(request):
    app.ctx.current_counter = 0
    return text("OK counter reset")


@app.websocket("/qr/feed")
async def feed(request: Request, ws: Websocket):
    app.ctx.open_web_sockets[ws] = ws
    async for msg in ws:
        await ws.send(msg)


@app.route('/qr')
async def handle_request(request):
    return await render("index.html", context={'counter': app.ctx.current_counter}, status=200)


app.run(host="0.0.0.0", port=8090)
