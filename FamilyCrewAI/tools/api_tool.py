import os
import requests
from requests.exceptions import RequestException


class APITool:
    def __init__(self):
        self.settings = self.load_settings()
        self.invocation_counts = {"openai": 0, "local": 0, "huggingface": 0}

    def load_settings(self):
        """
        Load API settings from environment variables securely.
        """
        return {
            "openai_api_key": os.getenv("OPENAI_API_KEY"),
            "local_model_endpoint": os.getenv("LOCAL_MODEL_ENDPOINT"),
            "huggingface_endpoint": os.getenv("HUGGINGFACE_ENDPOINT"),
        }

    def choose_model_dynamically(self, prompt):
        """
        Dynamically choose the model based on operational criteria such as prompt characteristics,
        failure rates, and response times. This method decides which LLM to use ('local', 'openai',
        or 'huggingface') by analyzing the prompt's length and keywords.

        Args:
        prompt (str): The input prompt to analyze and route to the appropriate LLM.

        Returns:
        str: The chosen model type.
        """

        # Criteria for choosing Hugging Face: use for longer, more complex prompts
        if (
            len(prompt) > 100
        ):  # This threshold for 'length' can be adjusted based on further analysis
            return "huggingface"

        # Criteria for using OpenAI: specific tasks like translation or complex queries
        elif "translate" in prompt or "summarize" in prompt:
            return "openai"

        # Default to local model for most other general and quick-response tasks
        else:
            return "local"

    def query(self, prompt, model_type=None):
        if model_type is None:
            model_type = self.choose_model_dynamically(prompt)

        if model_type == "openai":
            return self.query_openai(prompt)
        elif model_type == "local":
            return self.query_local(prompt)
        elif model_type == "huggingface":
            return self.query_huggingface(prompt)
        else:
            raise ValueError("Unsupported model type")

    def query_openai(self, prompt):
        """
        Query the OpenAI model.
        """
        headers = {"Authorization": f"Bearer {self.settings['openai_api_key']}"}
        data = {"prompt": prompt, "max_tokens": 150}
        try:
            response = requests.post(
                "https://api.openai.com/v1/engines/davinci-codex/completions",
                headers=headers,
                json=data,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["text"]
        except RequestException as e:
            print(f"Failed to query OpenAI: {str(e)}")
            return None

    def query_local(self, prompt):
        """
        Query the local model endpoint.
        """
        data = {"prompt": prompt}
        try:
            response = requests.post(self.settings["local_model_endpoint"], json=data)
            response.raise_for_status()
            return response.json()["result"]
        except RequestException as e:
            print(f"Failed to query local model: {str(e)}")
            return None

    def query_huggingface(self, prompt):
        """
        Query the Hugging Face model.
        """
        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
        data = {"inputs": prompt, "parameters": {"return_full_text": False}}
        try:
            response = requests.post(
                self.settings["huggingface_endpoint"], headers=headers, json=data
            )
            response.raise_for_status()
            return response.json()[0]["generated_text"]
        except RequestException as e:
            print(f"Failed to query Hugging Face: {str(e)}")
            return None
