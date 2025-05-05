from typing import Dict
from abc import ABC, abstractmethod

class PJGetUsersControllerInterface(ABC):
    
    @abstractmethod
    def list(self) -> Dict: pass
    