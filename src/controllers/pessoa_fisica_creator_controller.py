from typing import Dict
from src.models.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from .interfaces.pf_creator_controller import PFCreatorControllerInterface

class PessoaFisicaCreatorController(PFCreatorControllerInterface):
    def __init__(self, user_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def create(self, pessoa_fisica_info: Dict) -> Dict:
        renda_mensal = pessoa_fisica_info["renda_mensal"]
        idade = pessoa_fisica_info["idade"]
        nome_completo = pessoa_fisica_info["nome_completo"]
        celular = pessoa_fisica_info["celular"]
        email = pessoa_fisica_info["email"]
        categoria = pessoa_fisica_info["categoria"]
        saldo = pessoa_fisica_info["saldo"]

        self.__validate_info(renda_mensal, idade, 
                        nome_completo, celular, 
                        email, categoria, saldo)
        self.__insert_user_in_db(renda_mensal, idade, 
                        nome_completo, celular, 
                        email, categoria, saldo)
        response = self.__format_response(pessoa_fisica_info)
        return response
        
    
    def __validate_info(self, renda_mensal: any, idade: any, 
                        nome_completo: any, celular:any, 
                        email:any, categoria: any, saldo: any) -> None:
        if(
            not renda_mensal or not idade 
            or not nome_completo or not celular
            or not email or not categoria or not saldo
            or not isinstance(renda_mensal, float)
            or not isinstance(idade, int)
            or not isinstance(saldo, float)
            ): raise Exception("Invalid Input")
    
    def __insert_user_in_db(self, renda_mensal: float, idade: int, 
                    nome_completo: str, celular: str, 
                    email: str, categoria:str, saldo: float):
        self.__user_repository.create_user(
                        renda_mensal, idade, 
                        nome_completo, celular, 
                        email, categoria, saldo)

    def __format_response(self, pessoa_fisica_info) -> Dict:
        return{
            "data":{
                "type": "Pessoa Física",
                "count": 1,
                "attributes": pessoa_fisica_info
            }
        }
        
    


