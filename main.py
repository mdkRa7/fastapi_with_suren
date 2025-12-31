
from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn 

from keys_views import router as keys_router
from users.views import router as users_router

app = FastAPI()
app.include_router(keys_router)
app.include_router(users_router)

@app.get("/")
def hello_pidor():
    return {"dexter":"get blood"}

@app.get("/hello/")
def hello(name: str = "None"):
    name = name.strip().title()
    return {"name": f"{name}"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)