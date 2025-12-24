from collections import deque
from threading import Lock

class MessageQueue:
    def __init__(self, max_size=32):
        self.queue = deque(maxlen=max_size)
        self.lock = Lock()

    def push(self, message):
        with self.lock:
            self.queue.append(message)

    def pop(self):
        with self.lock:
            if self.queue:
                return self.queue.popleft()
        return None
