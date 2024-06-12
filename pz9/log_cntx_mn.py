import logging


class LogExecutionToFile:
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        logging.info("Execution started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Execution finished")
