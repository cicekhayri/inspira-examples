from inspira.decorators.http_methods import get, post
from inspira.decorators.path import path
from inspira.responses import JsonResponse
from inspira.requests import Request

from src.users.user_serializer import UserSerializer
from src.users.user_service import UserService


@path("/users")
class UserController:

    def __init__(self, user_service: UserService, serializer: UserSerializer):
        self._user_service = user_service
        self._serializer = serializer

    @get("/")
    async def get_users(self, request: Request):
        users = self._user_service.get_all_user()
        serialized_users = [self._serializer.user_all_fields(user) for user in users]

        context = {
            "users": serialized_users
        }

        return JsonResponse(context)

    @post("/create")
    async def create_user(self, request: Request):
        body = await request.json()
        name = body['name']
        email = body['email']

        success = self._user_service.create_user(name, email)

        if success:
            return JsonResponse({"message": "User successfully created"})
        else:
            return JsonResponse({"message": "Failed to create user"}, status_code=500)
