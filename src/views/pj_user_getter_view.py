from src.controllers.interfaces.pj_user_getter_controller import PJGetUsersControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PJGetUsersView(ViewInterface):
    def __init__(self, controller: PJGetUsersControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__controller.list()
        return HttpResponse(status_code= 200, body= response)
