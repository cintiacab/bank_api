from abc import ABC, abstractmethod

class PJWithdrawerControllerInterface(ABC):
    
    @abstractmethod
    def withdraw(self, user_id: int, withdrawal_amount: float) -> None: pass
