from typing import List
from src.models.entities.pessoa_fisica import PessoaFisicaTable
from src.models.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
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

    def get_users(self) -> List[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                users = database.session.query(PessoaFisicaTable).all()
                return users
            except Exception:
                return None

    def bank_statement(self, user_id: int) -> PessoaFisicaTable:
        with self.__db_connection as database:
            try:
                statement = (
                    database.session
                        .query(PessoaFisicaTable)
                        .filter(PessoaFisicaTable.id == user_id)
                        .one()
                )
                return statement
            except Exception:
                return None

    def withdraw_account(self, user_id: int, withdrawal_amount: float) -> None:
        with self.__db_connection as database:
            try: 
                database.session.query(PessoaFisicaTable).filter(
                PessoaFisicaTable.id == user_id).update(
                {PessoaFisicaTable.saldo: PessoaFisicaTable.saldo - withdrawal_amount})
                
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
