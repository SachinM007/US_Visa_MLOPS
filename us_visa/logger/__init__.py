import logging
import os

# ensures that your file paths are always relative to the project root, regardless of where the script is executed from

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    # format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    format=logging.BASIC_FORMAT,
    level=logging.DEBUG,
)