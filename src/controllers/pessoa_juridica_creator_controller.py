from typing import Dict
from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJuridicaCreatorController:
    def __init__(self, user_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def create(self, pessoa_juridica_info: Dict) -> Dict:
        faturamento = pessoa_juridica_info["faturamento"]
        idade = pessoa_juridica_info["idade"]
        nome_fantasia = pessoa_juridica_info["nome_fantasia"]
        celular = pessoa_juridica_info["celular"]
        email_corporativo = pessoa_juridica_info["email_corporativo"]
        categoria = pessoa_juridica_info["categoria"]
        saldo = pessoa_juridica_info["saldo"]

        self.__validate_info(faturamento, idade, 
                        nome_fantasia, celular, 
                        email_corporativo, categoria, saldo)
        self.__insert_user_in_db(faturamento, idade, 
                        nome_fantasia, celular, 
                        email_corporativo, categoria, saldo)
        response = self.__format_response(pessoa_juridica_info)
        return response
        
    
    def __validate_info(self, faturamento: float, idade: int, 
                    nome_fantasia: str, celular: str, 
                    email_corporativo: str, categoria:str, saldo: float) -> None:
        if(
            not faturamento or not idade 
            or not nome_fantasia or not celular
            or not email_corporativo or not categoria or not saldo
            or not isinstance(faturamento, float)
            or not isinstance(idade, int)
            or not isinstance(saldo, float)
            ): raise Exception("Invalid Input")
    
    def __insert_user_in_db(self, faturamento: float, idade: int, 
                    nome_fantasia: str, celular: str, 
                    email_corporativo: str, categoria:str, saldo: float):
        self.__user_repository.create_user(
                        faturamento, idade, 
                        nome_fantasia, celular, 
                        email_corporativo, categoria, saldo)

    def __format_response(self, pessoa_juridica_info) -> Dict:
        return{
            "data":{
                "type": "Pessoa Física",
                "count": 1,
                "attributes": pessoa_juridica_info
            }
        }
        
    


