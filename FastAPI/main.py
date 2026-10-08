from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/hahaha11/{name}")
async def say_hello(name: str):
    print("Hello,I am dev111222")
    return {"message": f"Hello {name}"}
