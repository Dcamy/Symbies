class TaskProcessor:
    def __init__(self, api_tool):
        """
        Initializes the TaskProcessor with an instance of the API Tool.

        Args:
        api_tool (APITool): The API tool used for querying language models.
        """
        self.api_tool = api_tool

    def process_tasks(self, file_path):
        """
        Processes tasks within a Markdown file.

        Args:
        file_path (str): The path to the Markdown file to be processed.
        """
        tasks = self.extract_tasks(file_path)
        for task in tasks:
            model_type = self.decide_model_for_task(task)
            result = self.execute_task(task, model_type)
            self.log_result(task, result)

    def extract_tasks(self, file_path):
        """
        Extracts actionable tasks from a Markdown file.

        Args:
        file_path (str): The path to the Markdown file.

        Returns:
        list: A list of tasks extracted from the file.
        """
        tasks = []
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(
                    "- [ ]"
                ):  # This is a simple way to identify tasks, customize as needed
                    tasks.append(line.strip())
        return tasks

    def decide_model_for_task(self, task):
        """
        Decides which LLM to use for a given task based on its content.

        Args:
        task (str): The task for which to decide the LLM.

        Returns:
        str: The type of LLM ('local', 'openai', or 'huggingface').
        """
        if "translate" in task:
            return "huggingface"
        elif "summarize" in task:
            return "openai"
        else:
            return "local"

    def execute_task(self, task, model_type):
        """
        Executes a task using the specified LLM.

        Args:
        task (str): The task to be executed.
        model_type (str): The type of LLM to use.

        Returns:
        str: The result of the task execution.
        """
        prompt = self.format_prompt(task)
        response = self.api_tool.query(model_type, prompt)
        return response

    def format_prompt(self, task):
        """
        Formats a task into a prompt suitable for LLM processing.

        Args:
        task (str): The task to be formatted.

        Returns:
        str: A formatted prompt.
        """
        return f"Please complete the following task: {task}"

    def log_result(self, task, result):
        """
        Logs the result of a task execution.

        Args:
        task (str): The task that was executed.
        result (str): The result from the LLM.
        """
        print(f"Task: {task}\nResult: {result}\n")
