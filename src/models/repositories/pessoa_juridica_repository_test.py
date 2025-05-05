from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_repository import PessoaJuridicaRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaJuridicaTable)],
                    [
                        PessoaJuridicaTable(
                            id =1, faturamento = 100000, idade = 5,
                            nome_fantasia = "Empresa Mega", celular = "7878-7878",
                            email_corporativo = "mega@email.com", categoria = "Categoria A", saldo = 1500000),
                        PessoaJuridicaTable(
                            id =2, faturamento = 300000, idade = 9,
                            nome_fantasia = "Transportadora Alfa", celular = "5656-5656",
                            email_corporativo = "alfa@email.com", categoria = "Categoria B", saldo = 2000000)
                    ]
                ),
            ]
        )
    
    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        pass

def test_bank_statement():
    mock_conn = MockConnection()
    repo = PessoaJuridicaRepository(mock_conn)
    repo.bank_statement(2)

    mock_query = mock_conn.session.query.return_value
    mock_filter = mock_query.filter.return_value

    mock_conn.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_query.filter.assert_called_once_with(PessoaJuridicaTable.id == 2)
    mock_filter.one.assert_called_once()

def test_withdraw_account():
    mock_conn = MockConnection()
    repo = PessoaJuridicaRepository(mock_conn)
    repo.withdraw_account(1, 50000)

    mock_query = mock_conn.session.query.return_value
    mock_filter = mock_query.filter.return_value

    mock_conn.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_query.filter.assert_called_once_with(PessoaJuridicaTable.id == 1)
    mock_filter.update.assert_called_once_with({PessoaJuridicaTable.saldo: PessoaJuridicaTable.saldo - 50000})
    