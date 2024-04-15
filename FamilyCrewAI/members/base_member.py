import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ..tools.api_tool import APITool

# Ensure api_tool.py is correctly located relative to this file


class BaseMember:
    def __init__(self, name, watch_directory):
        self.name = name
        self.watch_directory = watch_directory
        self.observer = Observer()
        self.api_tool = APITool()  # Instance of the API Tool
        self.setup_watcher()

    def setup_watcher(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_modified
        event_handler.on_created = self.on_created
        self.observer.schedule(event_handler, self.watch_directory, recursive=True)
        self.observer.start()

    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"Detected modification in: {event.src_path}")
            self.process_file(event.src_path)

    def on_created(self, event):
        if event.src_path.endswith(".md"):
            print(f"Detected new file: {event.src_path}")
            self.process_file(event.src_path)

    def process_file(self, filepath):
        print(f"Processing file: {filepath}")
        with open(filepath, "r", encoding="utf-8") as file:
            contents = file.read()
            # Decide which LLM to use based on contents or other criteria
            model_type = self.decide_llm(contents)
            response = self.api_tool.query(model_type, contents)
            print(f"Processed by {model_type} LLM: {response}")

    def decide_llm(self, contents):
        """
        Decide which LLM to use based on the contents of the file or other criteria.

        Args:
        contents (str): Content of the file being processed.

        Returns:
        str: Type of LLM ('local' or 'openai')
        """
        # Example simplistic decision logic
        if "advanced" in contents:
            return "huggingface"
        elif "complex" in contents:
            return "openai"
        else:
            return "local"

    def stop(self):
        self.observer.stop()
        self.observer.join()
