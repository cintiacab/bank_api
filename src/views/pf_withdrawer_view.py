from src.controllers.interfaces.pf_withdrawer_controller import PFWithdrawerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PFWithdrawerView(ViewInterface):
    def __init__(self, controller: PFWithdrawerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.param["user_id"]
        withdrawal_amount = http_request.body
        self.__controller.withdraw(user_id, withdrawal_amount)
        return HttpResponse(status_code=204)
