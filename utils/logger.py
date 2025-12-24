import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "sent_messages.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

def log_sent(message: str):
    logging.info(message)
