from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Harshita!"}

@app.get("/status")
def status():
    return {"status": "running", "mood": "chill"}

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"hello {name}!"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return{"item_id": item_id, "detail":"This is your item!"}