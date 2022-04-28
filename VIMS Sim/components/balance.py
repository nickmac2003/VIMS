import tkinter as tk

class Balance(tk.Frame):
  def __init__(self, parent, c):
    tk.Frame.__init__(self, parent, height=20, bg="white")

    # Card balance
    self.balanceFrame = tk.Frame(self, height=20, width=70, bg="white")
    self.balanceFrame.pack(padx=(20, 0), pady=(0, 4), side="right")

    #tk.Label(self.balanceFrame, image=c.coin, bg="white").pack(side="left")
    #tk.Label(self.balanceFrame, textvariable=c.coinBalance, bg="white").pack(side="right")

    # Machine coin balance
    self.coinFrame = tk.Frame(self, height=20, width=70, bg="white")
    self.coinFrame.pack(pady=(0, 4), side="left")

    #tk.Label(self.coinFrame, image=c.coin, bg="white").pack(side="left")
    #tk.Label(self.coinFrame, textvariable=c.machineBalance, bg="white").pack(side="right")