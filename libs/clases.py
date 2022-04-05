from tkinter import *

class Checkbar(Frame):
    def __init__(self, parent = None, picks=[], side=LEFT, anchor = W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = BooleanVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor,expand=YES)
            self.vars.append(var)
        for i in range(4):
            self.vars[i].set(True)
    def state(self):
        return list(map((lambda var: var.get()), self.vars))
    
