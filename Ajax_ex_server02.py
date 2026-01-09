from fastapi import *
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# 서버에서 사칙연산 계산기 구현
# PathParam으로 /연산자/항1/항2
# 우아한 URL
@app.get("/plus/{a}/{b}")
def plus(a:int, b:int) :
    print("더하기 결과=>", a, b, a + b)
    return a + b

@app.get("/min/{a}/{b}")
def minus(a:int, b:int) :
    print("빼기 결과=>", a, b, a - b)
    return a - b

@app.get("/mult/{a}/{b}")
def multiply(a:int, b:int) :
    print("곱하기 결과=>", a, b, a * b)
    return a * b

@app.get("/div/{a}/{b}")
def divide(a:int, b:int) :
    print("나누기 결과=>", a, b, a / b)
    return a / b
