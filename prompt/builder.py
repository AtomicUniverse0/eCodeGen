class PromptBuilder:
    def build_initial_prompt(self, user_query: str) -> str:
        raise NotImplementedError("This method is not implemented yet.")

    def build_error_prompt(self, user_query: str, error_message: str) -> str:
        raise NotImplementedError("This method is not implemented yet.")