from src.users.user import User


class UserSerializer:

    @staticmethod
    def serialize_only_email(user: User):
        return {
            "email": user.email
        }

    @staticmethod
    def user_all_fields(user: User):
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
