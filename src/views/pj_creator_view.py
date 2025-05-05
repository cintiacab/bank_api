from src.controllers.interfaces.pj_creator_controller import PJCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PJCreatorView:
    def __init__(self, controller: PJCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_info = http_request.body
        response = self.__controller.create(pessoa_juridica_info)
        return HttpResponse(status_code= 201, body= response)
