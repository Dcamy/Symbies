import logging
from datetime import datetime


class Logger:
    def __init__(self, name, log_file):
        """
        Initializes the logger with a specific log file and name.

        Args:
        name (str): Name of the logger to create.
        log_file (str): File path for the logging output.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(
            logging.DEBUG
        )  # Set to DEBUG to capture all levels of log messages

        # Create file handler which logs even debug messages
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)

        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)  # Set to ERROR to prevent flooding the console

        # Create formatter and add it to the handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def log(self, level, message):
        """
        Logs a message with the specified level.

        Args:
        level (str): Level of the log ('info', 'warning', 'debug', 'error', 'critical').
        message (str): Message to log.
        """
        if level.lower() == "info":
            self.logger.info(message)
        elif level.lower() == "warning":
            self.logger.warning(message)
        elif level.lower() == "debug":
            self.logger.debug(message)
        elif level.lower() == "error":
            self.logger.error(message)
        elif level.lower() == "critical":
            self.logger.critical(message)

    def log_decision(self, decision, reason):
        """
        Logs detailed decision-making process especially for LLM selection.

        Args:
        decision (str): The decision made (e.g., which LLM was selected).
        reason (str): The rationale behind the decision.
        """
        message = f"Decision: {decision}, Reason: {reason}"
        self.logger.debug(message)


# Example Usage
if __name__ == "__main__":
    logger = Logger("FamilyAILogger", "family_ai.log")
    logger.log("info", "Logger initialized")
    logger.log_decision(
        "Use Local LLM",
        "The prompt length was short, suitable for quick local processing.",
    )
