from inspira.decorators.http_methods import get
from inspira.decorators.path import path
from inspira.requests import Request
from inspira.responses import HttpResponse


@path("/sessions")
class SessionController:

    @get()
    async def index(self, request: Request):
        request.set_session("hayri", "yes")

        return HttpResponse("Session set successfully")

    @get("/get")
    async def get_session(self, request: Request):
        session = request.session

        if "hayri" in session:
            return HttpResponse("Hayri was in the session")
        else:
            return HttpResponse("Hayri was not in the session")

    @get("/remove")
    async def remove_session(self, request: Request):
        request.remove_session("hayri")

        return HttpResponse("Hayri was removed from the session")
