from fastapi import *
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# public 폴더를 정적 파일 경로로 등록(mount)
app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.get("/")
def root(message: str = "hello") :
    return {
        "message": message,
        "message length": len(message)
    }


# BasesModel을 상속받아서 Message클래스 선언
from pydantic import BaseModel

# 클라이언트에서 Ajax로 통신할때 JSON 데이터
# POST로 통신 할때는 JSON으로 데이터 전송
class Message(BaseModel):
    text: str

# post 메서드를 추가하고 postman으로 테스트 하기
# Content-Type: raw로 설정 후 JSON 데이터 전송
@app.post("/")
def root_post(message: Message) :
    return {
        "message": message.text,
        "message length": len(message.text)
    }


# Form 파라미터 전달 받기
@app.post("/login")
def login_post(username: str = Form(...)):
    return {
        "username": username
    }