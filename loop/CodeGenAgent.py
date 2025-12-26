from llm.base import BaseLLM
from compiler.base import BaseCompiler
from prompt.builder import PromptBuilder
from logging import Logger

class CodeGenAgent:
    def __init__(self, 
                 llm : BaseLLM,
                 compiler : BaseCompiler, 
                 promptBuilder : PromptBuilder,
                 logger : Logger,
                 maxIter = 3
                 ):
        self.llm = llm
        self.compiler = compiler
        self.promptBuilder = promptBuilder
        self.logger = logger
        self.maxIter = maxIter

    def run(self, user_query: str) -> str:
        raise NotImplementedError("This method is not implemented yet.")