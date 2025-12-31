from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/keys", tags=["Keys"])

@router.get("/")
def get_keys():
    return ["gg", 'dfdf']

@router.get("/latest/")
def get_latest_key():
    return {"latest": {"id": 344, "name": "accomplish"}}

@router.get("/{id_us}/")
def get_keys_by_id(id_us: Annotated[int, Path(ge=1, lt=100)]):
    return {
        "id_us":{
            "your id": id_us
        }
    }