from src.controllers.interfaces.pf_statement_shower_controller import PFStatementShowerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PFStatementShowerView:
    def __init__(self, controller: PFStatementShowerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.param["user_id"]
        response = self.__controller.show_statement(user_id)
        return HttpResponse(status_code= 200, body= response)
