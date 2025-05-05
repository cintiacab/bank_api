from abc import ABC, abstractmethod

class PFWithdrawerControllerInterface(ABC):
    
    @abstractmethod
    def withdraw(self, user_id: int, withdrawal_amount: float) -> None: pass
