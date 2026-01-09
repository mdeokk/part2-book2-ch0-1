from fastapi import *
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()

# public 폴더를 정적 파일 경로로 등록(mount)
app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.get("/")
def root(message: str = "hello") :
    print("GET - / 요청 받았다!")
    return {
        "message": message,
        "message length": len(message),
        "status": "200 OK"
    }

# 클라이언트가 접속하면 cnt가 하나 증가 하는 기능.
cnt = 0
@app.get("/count")
def count():
    global cnt
    cnt += 1
    now = datetime.now()
    return {
        "count": cnt,
        "dateStr": now.strftime("%Y-%m-%d %H:%M")
    }