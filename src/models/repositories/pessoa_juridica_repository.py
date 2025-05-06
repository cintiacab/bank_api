from typing import Dict, List
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

    def get_users(self) -> List[PessoaJuridicaTable]:
        with self.__db_connection as database:
            try:
                users = database.session.query(PessoaJuridicaTable).all()               
                return users
            except Exception:
                return None

    def bank_statement(self, user_id: int) -> PessoaJuridicaTable:
        with self.__db_connection as database:
            try:
                statement = (
                    database.session
                        .query(PessoaJuridicaTable)
                        .filter(PessoaJuridicaTable.id == user_id)
                        .one()
                )
                return statement
            except Exception:
                return None

    def withdraw_account(self, user_id: int, withdrawal_amount: float) -> None:
        with self.__db_connection as database:
            try: 
                database.session.query(PessoaJuridicaTable).filter(
                PessoaJuridicaTable.id == user_id).update(
                {PessoaJuridicaTable.saldo: PessoaJuridicaTable.saldo - withdrawal_amount["value"]})
                
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
