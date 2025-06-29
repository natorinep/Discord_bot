from threading import Thread

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.api_route("/", methods=["GET", "HEAD", "POST"])
async def root(request: Request):
    return {"message": "Server is Online.", "method": request.method}

def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)

def server_thread():
    t = Thread(target=start)
    t.start()