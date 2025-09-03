import logging

"""
Configure application-wide logging.

Logs are written both to 'app.log' and the console with timestamps,
log levels, logger names, filename, line number, function name, and message.
"""

# --------------------------
# Logging Configuration
# --------------------------

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | %(levelname)s | %(name)s | "
        "%(filename)s:%(lineno)d | %(funcName)s() | %(message)s"
    ),
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler("../app.log"),
        logging.StreamHandler()
    ],
    force=True
)

# Application logger
logger = logging.getLogger("Task")
