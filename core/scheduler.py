import threading
import time
from datetime import datetime

class Scheduler(threading.Thread):
    def __init__(self, conditions, queue, shutdown):
        super().__init__(daemon=True)
        self.conditions = conditions
        self.queue = queue
        self.shutdown = shutdown

    def run(self):
        while not self.shutdown.is_stopped():
            self.shutdown.wait_if_paused()
            now = datetime.now()
            for cond in self.conditions:
                if cond.is_true(now):
                    self.queue.push(cond.message)
            time.sleep(1)
