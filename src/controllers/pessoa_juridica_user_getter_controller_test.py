from typing import List
from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_user_getter_controller import PJGetUsersController

class MockRepository:
    def get_users(self) -> List[PessoaJuridicaTable]:
        return [
            PessoaJuridicaTable(
                id =1, faturamento = 100000, idade = 5,
                nome_fantasia = "Empresa Mega", celular = "7878-7878",
                email_corporativo = "mega@email.com", categoria = "Categoria A", saldo = 1500000),
            PessoaJuridicaTable(
                id =2, faturamento = 300000, idade = 9,
                nome_fantasia = "Transportadora Alfa", celular = "5656-5656",
                email_corporativo = "alfa@email.com", categoria = "Categoria B", saldo = 2000000)
        ]

def test_list():
    controller = PJGetUsersController(MockRepository())
    response = controller.list()

    expected_response = {
        'data': {
                'type': 'Pessoa Jurídica', 
                'count': 2, 
                'attributes': [
                    {'Id': 1, 'Name': 'Empresa Mega', 'Age': 5, 
                     'Phone': '7878-7878', 'E-mail': 'mega@email.com', 'Category': 'Categoria A'}, 
                    {'Id': 2, 'Name': 'Transportadora Alfa', 'Age': 9, 
                     'Phone': '5656-5656', 'E-mail': 'alfa@email.com', 'Category': 'Categoria B'}
                ]
        }
    }

    assert response == expected_response
