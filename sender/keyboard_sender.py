import threading
import time
import pyautogui
from utils.logger import log_sent

class KeyboardSender(threading.Thread):
    def __init__(self, queue, shutdown):
        super().__init__(daemon=True)
        self.queue = queue
        self.shutdown = shutdown

    def run(self):
        while not self.shutdown.is_stopped():
            self.shutdown.wait_if_paused()
            msg = self.queue.pop()
            if msg:
                pyautogui.write(msg.content, interval=0.02)
                pyautogui.press("enter")
                log_sent(msg.content)
            else:
                time.sleep(0.1)
