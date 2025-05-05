from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def create_user(self, faturamento: float, idade: int, 
                    nome_fantasia: str, celular: str, 
                    email_corporativo: str, categoria:str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = PessoaJuridicaTable(
                    faturamento = faturamento,
                    idade = idade,
                    nome_fantasia = nome_fantasia,
                    celular = celular,
                    email_corporativo = email_corporativo,
                    categoria = categoria,
                    saldo = saldo
                )
                database.session.add(pessoa_fisica_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_users(self):
        with self.__db_connection as database:
            try:
                users = (
                    database.session
                        .query(PessoaJuridicaTable)
                        .with_entities(
                            PessoaJuridicaTable.id,
                            PessoaJuridicaTable.nome_fantasia,
                            PessoaJuridicaTable.idade,
                            PessoaJuridicaTable.celular,
                            PessoaJuridicaTable.email_corporativo,
                            PessoaJuridicaTable.categoria)
                        .all()
                )
                return users
            except Exception:
                return None

    def bank_statement(self, user_id: int):
        with self.__db_connection as database:
            try:
                statement = (
                    database.session
                        .query(PessoaJuridicaTable)
                        .filter(PessoaJuridicaTable.id == user_id)
                        .with_entities(PessoaJuridicaTable.id,
                            PessoaJuridicaTable.nome_fantasia,
                            PessoaJuridicaTable.faturamento,
                            PessoaJuridicaTable.saldo)
                        .one()
                )
                return statement
            except Exception:
                return None

    def withdraw_account(self, user_id: int, withdraw_amount: float):
        with self.__db_connection as database:
            try: 
                database.session.query(PessoaJuridicaTable).filter(
                PessoaJuridicaTable.id == user_id).update(
                {PessoaJuridicaTable.saldo: PessoaJuridicaTable.saldo - withdraw_amount})
                
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
