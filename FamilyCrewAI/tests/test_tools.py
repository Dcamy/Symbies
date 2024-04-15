import unittest
from tools.api_tool import APITool
from tools.file_tool import FileTool
from tools.env_tool import EnvTool
from unittest.mock import patch, Mock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tools")))


class TestAPITool(unittest.TestCase):
    @patch("requests.post")
    def test_query_openai(self, mock_post):
        """
        Test querying OpenAI API.
        """
        # Configure the mock to return a custom response when called
        mock_response = Mock()
        mock_response.json.return_value = {"choices": [{"text": "mocked response"}]}
        mock_post.return_value = mock_response

        api_tool = APITool()
        response = api_tool.query_openai("test prompt")
        self.assertEqual(response, "mocked response")

        # Assert that the request was called exactly once and with expected URL
        mock_post.assert_called_once_with(
            "https://api.openai.com/v1/engines/davinci-codex/completions",
            headers={"Authorization": "Bearer fakekey-openai"},
            json={"prompt": "test prompt", "max_tokens": 150},
        )

    def test_query_selection(self):
        """Test API selection logic based on input prompt characteristics."""
        prompt_short = "Hello, world!"
        prompt_long = (
            "This is a long prompt" * 20
        )  # This will make the prompt significantly longer than 100 characters
        prompt_translate = "Translate this text, please."

        self.assertEqual(self.api_tool.choose_model_dynamically(prompt_short), "local")
        self.assertEqual(
            self.api_tool.choose_model_dynamically(prompt_long), "huggingface"
        )
        self.assertEqual(
            self.api_tool.choose_model_dynamically(prompt_translate), "openai"
        )

    def test_query_execution(self):
        """Test the execution of queries to each API."""
        # Mock responses would be used here in an actual implementation
        self.assertEqual(
            self.api_tool.query("local", "test prompt"), "Mocked local response"
        )
        self.assertEqual(
            self.api_tool.query("openai", "test prompt"), "Mocked OpenAI response"
        )
        self.assertEqual(
            self.api_tool.query("huggingface", "test prompt"),
            "Mocked Hugging Face response",
        )


class TestFileTool(unittest.TestCase):
    def setUp(self):
        """Initialize FileTool."""
        self.file_tool = FileTool()

    def test_read_write(self):
        """Test file reading and writing."""
        self.file_tool.write_file("test.txt", "Hello, world!")
        content = self.file_tool.read_file("test.txt")
        self.assertEqual(content, "Hello, world!")


class TestEnvTool(unittest.TestCase):
    @patch("os.getenv")
    def test_load_config(self, mock_getenv):
        """
        Test the loading of environment configurations.
        """
        mock_getenv.side_effect = lambda x: {
            "OPENAI_API_KEY": "fakekey-openai",
            "LOCAL_MODEL_ENDPOINT": "http://localhost:5000",
            "HUGGINGFACE_ENDPOINT": "http://api.huggingface.co",
        }.get(x)

        env_tool = EnvTool()
        self.assertEqual(env_tool.config["openai_api_key"], "fakekey-openai")
        self.assertEqual(
            env_tool.config["local_model_endpoint"], "http://localhost:5000"
        )
        self.assertEqual(
            env_tool.config["huggingface_endpoint"], "http://api.huggingface.co"
        )


# Additional tests can be added as needed

if __name__ == "__main__":
    unittest.main()
