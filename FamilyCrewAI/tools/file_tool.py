import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileTool:
    def __init__(self, directory):
        """
        Initialize the FileTool with a directory to watch for file changes.

        Args:
        directory (str): The directory path to watch.
        """
        self.directory = directory
        self.observer = Observer()
        self.start_watcher()

    def start_watcher(self):
        """
        Sets up the directory watcher to monitor for file changes.
        """
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_modified
        event_handler.on_created = self.on_created
        self.observer.schedule(event_handler, self.directory, recursive=True)
        self.observer.start()

    def on_modified(self, event):
        """
        Handle the 'modified' event for files.

        Args:
        event (Event): File system event object representing the file modifications.
        """
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")

    def on_created(self, event):
        """
        Handle the 'created' event for files.

        Args:
        event (Event): File system event object representing the file creations.
        """
        if event.is_directory:
            return
        print(f"File created: {event.src_path}")

    def read_file(self, filepath):
        """
        Reads the content of a file.

        Args:
        filepath (str): The path to the file to read.

        Returns:
        str: The content of the file.
        """
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    def write_file(self, filepath, content):
        """
        Writes content to a file.

        Args:
        filepath (str): The path to the file to write.
        content (str): The content to write to the file.
        """
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Content written to {filepath}")

    def stop_watcher(self):
        """
        Stops the directory watcher.
        """
        self.observer.stop()
        self.observer.join()
        print("File watcher stopped.")
