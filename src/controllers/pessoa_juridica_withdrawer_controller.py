from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from .interfaces.pj_withdrawer_controller import PJWithdrawerControllerInterface

class PJWithdrawerController(PJWithdrawerControllerInterface):
    def __init__(self, user_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def withdraw(self, user_id: int, withdrawal_amount: float) -> None:
        self.__validate_amount(withdrawal_amount)
        self.__user_repository.withdraw_account(user_id, withdrawal_amount)

    def __validate_amount(self, withdrawal_amount: float) -> None:
        if withdrawal_amount > 50000.00:
            raise Exception("The amount exceeds your daily withdrawal limit")
