import os


class EnvTool:
    def __init__(self):
        """
        Initialize the environment tool, loading all necessary configurations from environment variables.
        """
        self.config = self.load_config()

    def load_config(self):
        """
        Loads configuration settings from environment variables.

        Returns:
        dict: A dictionary containing all configuration settings.
        """
        return {
            "openai_api_key": self.get_env_variable("OPENAI_API_KEY"),
            "local_model_endpoint": self.get_env_variable("LOCAL_MODEL_ENDPOINT"),
            "huggingface_api_key": self.get_env_variable(
                "HUGGINGFACE_API_KEY"
            ),  # New variable for Hugging Face
            "database_url": self.get_env_variable(
                "DATABASE_URL"
            ),  # Example of another config
        }

    def get_env_variable(self, var_name):
        """
        Safely retrieve environment variables.

        Args:
        var_name (str): The environment variable key.

        Returns:
        str: The value of the environment variable.
        """
        value = os.getenv(var_name)
        if value is None:
            raise EnvironmentError(
                f"Required environment variable '{var_name}' is not set."
            )
        return value

    def update_config(self, var_name, var_value):
        """
        Update the configuration setting dynamically if needed.

        Args:
        var_name (str): The environment variable key to update.
        var_value (str): The new value for the environment variable.
        """
        os.environ[var_name] = var_value
        self.config[var_name] = var_value  # Update the local cache as well


# Usage example:
# env_tool = EnvTool()
# print(env_tool.config['openai_api_key'])  # Safely access the OpenAI API Key
