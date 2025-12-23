import logging
import os
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists("logs"):
            os.makedirs("logs")

        log_file = f"logs/automation_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )
        return logging

