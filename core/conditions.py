from datetime import datetime
from utils.safe_eval import safe_eval

class TimeCondition:
    def __init__(self, expression: str, message):
        self.expression = expression
        self.message = message

    def is_true(self, now: datetime):
        context = {
            "h": now.hour,
            "m": now.minute,
            "s": now.second
        }
        try:
            return safe_eval(self.expression, context)
        except Exception:
            return False
