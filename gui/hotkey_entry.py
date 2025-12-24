import tkinter as tk

class HotkeyEntry(tk.Entry):
    def __init__(self, master):
        super().__init__(master)
        self.bind("<Key>", self._capture)

    def _capture(self, event):
        parts = []
        if event.state & 0x4:
            parts.append("ctrl")
        if event.state & 0x20000:
            parts.append("alt")
        parts.append(event.keysym.lower())
        self.delete(0, tk.END)
        self.insert(0, "+".join(parts))
        return "break"
