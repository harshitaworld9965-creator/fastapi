from fastapi import FastAPI
from routes.users import router as users_router
from routes.items import router as items_router

app = FastAPI()

app.include_router(users_router)
app.include_router(items_router)

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project!"}
