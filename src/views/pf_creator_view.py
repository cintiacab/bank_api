from src.controllers.interfaces.pf_creator_controller import PFCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PFCreatorView(ViewInterface):
    def __init__(self, controller: PFCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_info = http_request.body
        response = self.__controller.create(pessoa_fisica_info)
        return HttpResponse(status_code= 201, body= response)
