from src.models.entities.pessoa_fisica import PessoaFisicaTable
from src.models.interfaces.user_repository import UserRepositoryInterface

class PessoaFisicaRepository(UserRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_user(self, renda_mensal: float, idade: int, 
                    nome_completo: str, celular: str, 
                    email: str, categoria:str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = PessoaFisicaTable(
                    renda_mensal = renda_mensal,
                    idade = idade,
                    nome_completo = nome_completo,
                    celular = celular,
                    email = email,
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
                        .query(PessoaFisicaTable)
                        .with_entities(
                            PessoaFisicaTable.id,
                            PessoaFisicaTable.nome_completo,
                            PessoaFisicaTable.idade,
                            PessoaFisicaTable.celular,
                            PessoaFisicaTable.email,
                            PessoaFisicaTable.categoria)
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
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == user_id)
                        .with_entities(PessoaFisicaTable.id,
                            PessoaFisicaTable.nome_completo,
                            PessoaFisicaTable.renda_mensal,
                            PessoaFisicaTable.saldo)
                        .one()
                )
                return statement
            except Exception:
                return None

    def withdraw_account(self, user_id: int, withdraw_amount: float):
        with self.__db_connection as database:
            try: 
                database.session.query(PessoaFisicaTable).filter(
                PessoaFisicaTable.id == user_id).update(
                {PessoaFisicaTable.saldo: PessoaFisicaTable.saldo - withdraw_amount})
                
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
