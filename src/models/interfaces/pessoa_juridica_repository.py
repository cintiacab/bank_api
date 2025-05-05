from abc import ABC, abstractmethod

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, faturamento: float, idade: int, 
                        nome_fantasia: str, celular: str, 
                        email_corporativo: str, categoria:str, saldo: float): pass

    @abstractmethod
    def get_users(self): pass

    @abstractmethod
    def bank_statement(self, user_id: int): pass

    @abstractmethod
    def withdraw_account(self, user_id: int, withdraw_amount: float): pass
