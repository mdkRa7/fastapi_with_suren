from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn 


app = FastAPI()

class CreateEmails(BaseModel):
    email: EmailStr 

@app.get("/")
def hello_pidor():
    return {"dexter":"get blood"}

@app.get("/hello/")
def hello(name: str = "None"):
    name = name.strip().title()
    return {"name": f"{name}"}

@app.get("/keys/")
def get_keys():
    return ["gg", 'dfdf']


@app.post("/users/")
def post_email(user: CreateEmails):
    return {
        "message": "success",
        "email": user.email, 
    }


@app.get("/keys/latest/")
def get_latest_key():
    return {"latest": {"id": 344, "name": "accomplish"}}

@app.get("/keys/{id_us}/")
def get_keys_by_id(id_us: int):
    return {
        "id_us":{
            "your id": id_us
        }
    }



if __name__ == "__main__":
    uvicorn.run("legenda:app", reload=True)