from pytest import raises
from .pessoa_fisica_creator_controller import PessoaFisicaCreatorController

class MockRepository:
    def create_user(self, renda_mensal: float, idade: int, 
                    nome_completo: str, celular: str, 
                    email: str, categoria:str, saldo: float) -> None:
        pass

def test_create():
    pessoa_fisica_info ={
        "renda_mensal" : 8000.00,
        "idade" : 28,
        "nome_completo" : "Cintia Cabral",
        "celular" : "7878-7878",
        "email" : "cintia@email.com",
        "categoria" : "Categoria A",
        "saldo" : 53000.00
    }
    controller = PessoaFisicaCreatorController(MockRepository())
    response = controller.create(pessoa_fisica_info)

    assert response["data"]["type"] == "Pessoa Física"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_fisica_info

def test_create_error():
    pessoa_fisica_info ={
        "renda_mensal" : 8000.00,
        "idade" : 28,
        "nome_completo" : "Cintia Cabral",
        "celular" : "7878-7878",
        "email" : "cintia@email.com",
        "categoria" : "Categoria A",
        "saldo" : "53000.00"
    }
    controller = PessoaFisicaCreatorController(MockRepository())

    with raises(Exception):
        controller.create(pessoa_fisica_info)
