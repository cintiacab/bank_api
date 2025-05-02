from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .pessoa_fisica_repository import PessoaFisicaRepository
from src.models.entities.pessoa_fisica import PessoaFisicaTable

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaFisicaTable)],
                    [
                        PessoaFisicaTable(
                            id =1, renda_mensal = 5000, idade = 28,
                            nome_completo = "Cintia Maria da Silva", celular = "7878-7878",
                            email = "cmds@email.com", categoria = "Categoria A", saldo = 10500),
                        PessoaFisicaTable(
                            id =2, renda_mensal = 4500, idade = 56,
                            nome_completo = "Antônio Ronildo", celular = "5656-5656",
                            email = "antonio@email.com", categoria = "Categoria B", saldo = 17800)
                    ]
                ),
            ]
        )
    
    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        pass

def test_create_user():
    mock_conn = MockConnection()
    repo = PessoaFisicaRepository(mock_conn)
    repo.create_user(10000, 30, "Nome de Teste", "1000-1000", "email_teste@email.com", "Categoria Teste", 25000)

    mock_conn.session.add.assert_called_once()
    mock_conn.session.query.assert_not_called()

def test_get_users():
    mock_conn = MockConnection()
    repo = PessoaFisicaRepository(mock_conn)
    repo.get_users()

    mock_query = mock_conn.session.query.return_value
    mock_with_entities = mock_query.with_entities.return_value

    mock_conn.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_query.with_entities.assert_called_once_with(
                            PessoaFisicaTable.id,
                            PessoaFisicaTable.nome_completo,
                            PessoaFisicaTable.idade,
                            PessoaFisicaTable.celular,
                            PessoaFisicaTable.email,
                            PessoaFisicaTable.categoria)
    mock_with_entities.all.assert_called_once()
