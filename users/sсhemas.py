from fastapi import Path
from pydantic import BaseModel, EmailStr
from typing import Annotated  # noqa
from annotated_types import MaxLen, MinLen


class CreateEmails(BaseModel):
    name: Annotated[str, MinLen(1), MaxLen(10)]
    age: Annotated[int, Path(ge=1, le=100)]
    email: EmailStr
