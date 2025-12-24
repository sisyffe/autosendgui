import tkinter as tk
from core.conditions import TimeCondition
from core.message import Message

class AdvancedMode:
    def __init__(self, app):
        self.app = app
        self.frame = tk.LabelFrame(text="Mode avancé")

        tk.Label(self.frame, text="Condition (h,m,s)").pack()
        self.cond = tk.Entry(self.frame, width=50)
        self.cond.pack()

        tk.Label(self.frame, text="Message").pack()
        self.msg = tk.Entry(self.frame)
        self.msg.pack()

        tk.Button(self.frame, text="Ajouter règle", command=self.add).pack()

    def add(self):
        self.app.conditions.append(
            TimeCondition(self.cond.get(), Message(self.msg.get()))
        )
