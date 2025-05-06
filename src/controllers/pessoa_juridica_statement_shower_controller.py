from typing import Dict
from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from .interfaces.pj_statement_shower_controller import PJStatementShowerControllerInterface

class PJStatementShowerController(PJStatementShowerControllerInterface):
    def __init__(self, user_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def show_statement(self, user_id: int) -> Dict:
        statement = self.__get_statement_in_db(user_id)
        response = self.__format_response(statement)
        return response
    
    def __get_statement_in_db(self, user_id: int):
        statement = self.__user_repository.bank_statement(user_id)
        return statement
    
    def __format_response(self, statement: Dict):
        return {
            "data":{
                "type": "Bank Statement",
                "attributes": ({"Id": statement.id, 
                                "Name": statement.nome_fantasia, 
                                "Revenue": statement.faturamento, 
                                "Balance": statement.saldo,})
            }
        }
