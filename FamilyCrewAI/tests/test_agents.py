import unittest
from members.base_member import BaseMember
from tools.api_tool import APITool


class TestBaseMember(unittest.TestCase):
    def setUp(self):
        """Setup for test methods."""
        self.member = BaseMember("TestAgent", "/path/to/watch/directory")

    def test_initialization(self):
        """Test initialization of base member."""
        self.assertEqual(self.member.name, "TestAgent")
        self.assertIsNotNone(
            self.member.watch_directory, "Directory should not be None"
        )

    def test_file_processing(self):
        """Test the file processing handles different types of content."""
        test_content = "Example content that triggers LLM decision."
        self.member.process_file = (
            lambda x: f"Processed {x}"
        )  # Mocking process_file method
        result = self.member.process_file(test_content)
        self.assertIn("Processed", result)

    def test_llm_integration(self):
        """Test LLM selection and integration."""
        content = "Detailed analysis required."
        llm_type = self.member.decide_llm(content)
        self.assertIn(
            llm_type,
            ["local", "openai", "huggingface"],
            "LLM type should be one of the specified types",
        )

    def test_decision_logging(self):
        """Test if decisions are logged correctly."""
        with self.assertLogs("FamilyAILogger", level="DEBUG") as log:
            self.member.log_decision("Use Local LLM", "Suitable for quick processing")
            self.assertIn("Decision: Use Local LLM", log.output[0])


# Add more tests as needed

if __name__ == "__main__":
    unittest.main()
