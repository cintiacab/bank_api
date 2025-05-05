from abc import ABC, abstractmethod

class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, renda_mensal: float, idade: int, 
                        nome_completo: str, celular: str, 
                        email: str, categoria:str, saldo: float): pass

    @abstractmethod
    def get_users(self): pass

    @abstractmethod
    def bank_statement(self, user_id: int): pass

    @abstractmethod
    def withdraw_account(self, user_id: int, withdraw_amount: float): pass
