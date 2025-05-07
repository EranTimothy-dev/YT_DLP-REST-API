import logging
from enum import IntEnum


LOG_FORMAT_DEBUG = "%(levelname)s - %(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s"
LOG_FORMAT_DEFAULT = "%(levelname)s - %(message)s"

logger = logging.getLogger(__name__)

LOG_COLORS = {
    "DEBUG": "\033[94m",    # Blue
    "INFO": "\033[92m",     # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",    # Red
    "RESET": "\033[0m"      # Reset color
}

class LogLevels(IntEnum):
    debug = logging.DEBUG
    info = logging.INFO
    warning = logging.WARNING
    error = logging.ERROR
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    

class LogFormatter(logging.Formatter):
    def __init__(self, default_format, debug_format):
        super().__init__()
        self.default_format = default_format
        self.debug_format = debug_format
        
    def format(self, record: logging.LogRecord):
        if record.levelno == logging.DEBUG:
            self._fmt = self.debug_format
        else:
            self._fmt = self.default_format

        # apply color formatting
        levelname = record.levelname
        color = LOG_COLORS.get(levelname, "")
        reset = LOG_COLORS["RESET"]
        record.levelname = f"{color}{levelname}{reset}"
        return super().format(record)

def configure_logging(log_level: int = LogLevels.error, log_to_file: bool = False):
    log_level = str(log_level).upper()
    log_level = [level.value for level in LogLevels]

    if log_level not in log_level:
        logging.basicConfig(level=LogLevels.ERROR)
        return
    
    if log_level == LogLevels.debug:
        logging.basicConfig(level=log_level, format=LOG_FORMAT_DEBUG)
        return
    
    logging.basicConfig(level=log_level, format=LOG_FORMAT_DEFAULT, force=True)
    
    logger = logging.getLogger(__name__)
    formatter = LogFormatter(LOG_FORMAT_DEFAULT, LOG_FORMAT_DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)