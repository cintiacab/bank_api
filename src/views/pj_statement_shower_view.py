from src.controllers.interfaces.pj_statement_shower_controller import PJStatementShowerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PJStatementShowerView(ViewInterface):
    def __init__(self, controller: PJStatementShowerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.param["user_id"]
        response = self.__controller.show_statement(user_id)
        return HttpResponse(status_code= 200, body= response)
