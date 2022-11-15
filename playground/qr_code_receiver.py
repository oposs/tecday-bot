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
        let e = event;
        console.log(e.data);
        let count = document.getElementById('ctr').innerHTML;
        console.log(parseInt(count,10) + 1);
        ctr = parseInt(count,10) + 1;
        document.getElementById('ctr').innerHTML = ctr
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

"""
    <html><head>
    </head>
      <body><h1>Main</h1>
        <div><form><input id="in" type="text" method="post"></form></div>
        <div><ul id="out"></ul></div>
     </body>
     <script>
    const ws = new WebSocket("ws://" + location.host + '/feed');
    ws.onmessage = event => {
      let e = event;
      console.log(e.data);
      let out = document.getElementById('out');
      out.innerHTML += `<li><p>${e.data}</p></li>`;
    }
    document.querySelector('form').addEventListener('submit', (event) => {
      event.preventDefault();
      let message = document.querySelector("#in").value;
      ws.send(message);
      document.querySelector("#in").value = "";
    })
    </script>
    </html>
"""
