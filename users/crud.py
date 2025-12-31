from users.sсhemas import CreateEmails


def create_user(user_in: CreateEmails) -> dict:
    user = user_in.model_dump()
    print(user)
    return {
        "message": "success",
        "user": user,
    }
