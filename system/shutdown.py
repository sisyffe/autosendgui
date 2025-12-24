import threading

class ShutdownController:
    def __init__(self):
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.pause_event.set()

    def stop(self):
        self.stop_event.set()

    def pause(self):
        self.pause_event.clear()

    def resume(self):
        self.pause_event.set()

    def is_stopped(self):
        return self.stop_event.is_set()

    def wait_if_paused(self):
        self.pause_event.wait()
