from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass