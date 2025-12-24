import tkinter as tk
from gui.simple_mode import SimpleMode
from gui.advanced_mode import AdvancedMode
from gui.hotkey_entry import HotkeyEntry
from system.hotkey_listener import HotkeyListener
from core.queue_manager import MessageQueue
from sender.keyboard_sender import KeyboardSender
from core.scheduler import Scheduler

class MainWindow:
    def __init__(self, shutdown):
        self.shutdown = shutdown
        self.root = tk.Tk()
        self.root.title("Auto Messenger")

        self.queue = MessageQueue()
        self.conditions = []

        self._build_controls()

        self.hotkey = HotkeyListener(
            shutdown,
            hotkey=self.hotkey_entry.get(),
            on_pause=self._pause_from_hotkey
        )
        self.hotkey.start()

    def _build_controls(self):
        top = tk.Frame(self.root)
        top.pack()

        tk.Label(top, text="Hotkey arrêt").pack(side=tk.LEFT)
        self.hotkey_entry = HotkeyEntry(top)
        self.hotkey_entry.insert(0, "ctrl+alt+s")
        self.hotkey_entry.pack(side=tk.LEFT)

        tk.Button(top, text="Arrêt définitif", command=self.shutdown.stop).pack()

        SimpleMode(self).frame.pack()
        AdvancedMode(self).frame.pack()

    def _pause_from_hotkey(self):
        self.shutdown.pause()
        self.root.after(0, self.root.deiconify)

    def run(self):
        sender = KeyboardSender(self.queue, self.shutdown)
        scheduler = Scheduler(self.conditions, self.queue, self.shutdown)
        sender.start()
        scheduler.start()
        self.root.mainloop()
