from src.controllers.interfaces.pf_user_getter_controller import PFGetUsersControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PFGetUsersView:
    def __init__(self, controller: PFGetUsersControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__controller.list()
        return HttpResponse(status_code= 200, body= response)
