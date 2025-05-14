import logging
import sys
from enum import StrEnum


LOG_FORMAT_DEBUG = "%(levelname)s:    %(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s"
LOG_FORMAT_DEFAULT = "%(levelname)s:     %(message)s"

logger = logging.getLogger(__name__)

LOG_COLORS = {
    "DEBUG": "\033[94m",    # Blue
    "INFO": "\033[92m",     # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",    # Red
    "RESET": "\033[0m"      # Reset color
}

class LogLevels(StrEnum):
    info = "INFO"
    warning = "WARN"
    error = "ERROR"
    debug = "DEBUG"



class LogFormatter(logging.Formatter):
    def __init__(self, default_format, debug_format):
        super().__init__()
        self.default_format = default_format
        self.debug_format = debug_format
        
    def format(self, record: logging.LogRecord):
        if record.levelname == "DEBUG":
            self._style._fmt = self.debug_format
        else:
            self._style._fmt = self.default_format

        # apply color formatting
        levelname = record.levelname
        color = LOG_COLORS.get(levelname, "")
        reset = LOG_COLORS["RESET"]
        record.levelname = f"{color}{levelname}{reset}"
        return super().format(record)

def configure_logging(log_level: str = LogLevels.error):
    log_level = str(log_level).upper()
    log_levels = [level.value for level in LogLevels]

    if log_level not in log_levels:
        logging.basicConfig(level=LogLevels.error, format=LOG_FORMAT_DEFAULT)
        return

    if log_level == LogLevels.debug:
        handler = logging.StreamHandler(sys.stdout)
        formatter = LogFormatter(LOG_FORMAT_DEFAULT, LOG_FORMAT_DEBUG)
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.handlers.clear()
        logger.setLevel(log_level)
        logger.addHandler(handler)
        return
    

    
    handler = logging.StreamHandler(sys.stdout)
    formatter = LogFormatter(LOG_FORMAT_DEFAULT, LOG_FORMAT_DEBUG)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.handlers.clear()
    logger.setLevel(log_level)
    logger.addHandler(handler)

    

if __name__ == "__main__":
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

    for logger in loggers:
        print(logger)
