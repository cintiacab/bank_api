from src.models.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_statement_shower_controller import PFStatementShowerController

class MockRepository:
    def bank_statement(self, user_id: int):
        return PessoaFisicaTable(id =1, renda_mensal = 5000, idade = 28,
                nome_completo = "Cintia Maria da Silva", celular = "7878-7878",
                email = "cmds@email.com", categoria = "Categoria A", saldo = 10500)
    
def test_show_statement():
    controller = PFStatementShowerController(MockRepository())
    response = controller.show_statement(1)

    expected_response = {'data': {'type': 'Bank Statement', 
                                  'attributes':
                                    {'Id': 1, 'Name': 'Cintia Maria da Silva', 
                                     'Income': 5000, 'Balance': 10500}
                                }
                        }
    
    assert response == expected_response
