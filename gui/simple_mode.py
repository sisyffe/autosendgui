import tkinter as tk
from core.conditions import TimeCondition
from core.message import Message

class SimpleMode:
    def __init__(self, app):
        self.app = app
        self.frame = tk.LabelFrame(text="Mode simple")

        tk.Label(self.frame, text="Message").pack()
        self.msg = tk.Entry(self.frame)
        self.msg.pack()

        tk.Label(self.frame, text="Fréquence (s)").pack()
        self.freq = tk.Entry(self.frame)
        self.freq.pack()

        tk.Button(self.frame, text="Ajouter", command=self.add).pack()

    def add(self):
        message = Message(self.msg.get())
        freq = int(self.freq.get())
        expr = f"s % {freq} == 0"
        self.app.conditions.append(TimeCondition(expr, message))
