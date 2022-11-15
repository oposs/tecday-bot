from sanic import Sanic, response, Request, Websocket, text

app = Sanic("TecDaysQRReceiver")


@app.get("/counter_inc")
async def send_msg(request):
    await app.ctx.current_ws.send('inc')
    return text("OK")


@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    app.ctx.current_ws = ws
    async for msg in ws:
        await ws.send(msg)


@app.route('/')
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
    const ws = new WebSocket("ws://" + location.host + '/feed');
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


app.run(host="0.0.0.0", port=8000)
