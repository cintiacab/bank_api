from typing import Dict
from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PJStatementShowerController:
    def __init__(self, user_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def show_statement(self):
        statement = self.__get_statement_in_db
        response = self.__format_response(statement)
        return response
    
    def __get_statement_in_db(self):
        statement = self.__user_repository.bank_statement()
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
