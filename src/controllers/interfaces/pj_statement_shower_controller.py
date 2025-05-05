from typing import Dict
from abc import ABC, abstractmethod

class PJStatementShowerControllerInterface(ABC):

    @abstractmethod
    def show_statement(self, user_id: int) -> Dict: pass
