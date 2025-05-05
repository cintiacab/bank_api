from typing import Dict, List
from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PJGetUsersController:
    def __init__(self, user_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def list(self) -> Dict:
        users = self.__get_users_in_db()
        response = self.__format_response(users)
        return response

    def __get_users_in_db(self) -> List[PessoaJuridicaTable]:
        users = self.__user_repository.get_users()
        return users

    def __format_response(self, users: List[PessoaJuridicaTable]) -> Dict:
        formatted_response = []
        for user in users:
            formatted_response.append({"Id": user.id, 
                                       "Name": user.nome_fantasia, 
                                       "Age": user.idade, 
                                       "Phone": user.celular,
                                       "E-mail": user.email_corporativo,
                                       "Category" : user.categoria})

        return {
            "data":{
                "type": "Pessoa Jurídica",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
