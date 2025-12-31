from fastapi import APIRouter

router = APIRouter(tags=["Users"], prefix="/users")

from users.sсhemas import CreateEmails
from users import crud


@router.post("/")
def post_email(user_: CreateEmails):
    return crud.create_user(user_in=user_)
