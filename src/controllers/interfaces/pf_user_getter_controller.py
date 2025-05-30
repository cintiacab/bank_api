from typing import Dict
from abc import ABC, abstractmethod

class PFGetUsersControllerInterface(ABC):
    
    @abstractmethod
    def list(self) -> Dict: pass
    