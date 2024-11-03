from abc import ABC, abstractmethod

class BaseTool(ABC):
    @abstractmethod
    def get_available_tasks(self):
        pass
