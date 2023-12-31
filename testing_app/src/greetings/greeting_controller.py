from inspira.decorators.http_methods import get
from inspira.decorators.path import path
from inspira.responses import JsonResponse
from inspira.requests import Request


@path("/greetings")
class GreetingController:

    @get()
    async def index(self, request: Request):
        context = {"variable": "value"}

        return JsonResponse(context)
