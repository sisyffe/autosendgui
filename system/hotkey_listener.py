import keyboard
import threading

class HotkeyListener(threading.Thread):
    def __init__(self, shutdown, hotkey, on_pause):
        super().__init__(daemon=True)
        self.shutdown = shutdown
        self.hotkey = hotkey
        self.on_pause = on_pause

    def run(self):
        keyboard.add_hotkey(self.hotkey, self.on_pause)
        keyboard.wait()
