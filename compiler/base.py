from abc import ABC, abstractmethod

class CompileResult:
    def __init__(self, success: bool, stdout: str, stderr: str):
        self.success = success
        self.stdout = stdout
        self.stderr = stderr

class Compiler(ABC):
    @abstractmethod
    def compile(self, code: str) -> CompileResult:
        pass