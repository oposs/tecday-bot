from sanic import Sanic, response, Request, Websocket, text
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
    return text('OK')


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
    return response.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>QR Code receiver</title>
</head>
<style>
    div.centered {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 20em;
    }
</style>
<script>
    const ws = new WebSocket("wss://" + location.host + '/qr/feed');
    ws.onmessage = event => {
        console.log(event.data);
        let count = document.getElementById('ctr').innerHTML;
        console.log(parseInt(count,10) + 1);
        document.getElementById('ctr').innerHTML = parseInt(count,10) + 1;
    }
</script>
<body>
<div class="centered" id="ctr">
    0
</div>
</body>
</html>
    """)


app.run(host="0.0.0.0", port=8090)
