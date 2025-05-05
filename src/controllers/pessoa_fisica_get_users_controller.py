from typing import Dict, List
from src.models.entities.pessoa_fisica import PessoaFisicaTable
from src.models.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PFGetUsersController:
    def __init__(self, user_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def list(self) -> Dict:
        users = self.__get_users_in_db()
        response = self.__format_response(users)
        return response

    def __get_users_in_db(self) -> List[PessoaFisicaTable]:
        users = self.__user_repository.get_users()
        return users

    def __format_response(self, users: List[PessoaFisicaTable]) -> Dict:
        formatted_response = []
        for user in users:
            formatted_response.append({"Id": user.id, 
                                       "Name": user.nome_completo, 
                                       "Age": user.idade, 
                                       "Mobile": user.celular,
                                       "E-mail": user.email,
                                       "Category" : user.categoria})

        return {
            "data":{
                "type": "Pessoa Física",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
