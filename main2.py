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
    
# 서버의 cnt와 클라이언트의 cnt가 동일한지 비교
# 파라미터로 클라이언트의 cnt를 요청 받기
# 서버의 cnt가 클라이언트의 cnt보다 큰값이면 새 cnt 보내기
@app.get("/check/{client_cnt}")
def check_cnt(client_cnt):
    print("client_cnt:", client_cnt)
    if cnt > int(client_cnt) :
        now = datetime.now()
        return {
            "count": cnt,
            "dateStr": now.strftime("%Y-%m-%d %H:%M")
        }
    else :
        return None