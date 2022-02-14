# pyright: reportMissingImports=false
import tkinter as tk

import configs.screen as screen
import configs.constants as constants
from connector import finishAndPay, updateTicketBalance

def receiptWindow(config, parent, c):
  basket      = c.basket
  subtotal    = c.subtotal.get()
  payCashIcon = config["payCashIcon"]
  payCardIcon = config["payCardIcon"]

  newWindow = tk.Toplevel(parent)
  newWindow.title("Receipt")
  newWindow.resizable(False, False)
  newWindow.configure(background="white", pady=20, padx=10)

  # Parent Frame
  infoFrame = tk.Frame(newWindow, bg="white")
  infoFrame.pack()

  # Receipt header
  tk.Label(infoFrame, text="Soda Vending Machine", bg="white", font=constants.SUB_HEADER).pack()
  tk.Label(infoFrame, text="*" * 43, bg="white").pack()

  # Table Frames
  nameFrame = tk.Frame(infoFrame, bg="white")
  nameFrame.pack(side="left")

  priceFrame = tk.Frame(infoFrame, bg="white")
  priceFrame.pack(side="right")

  tk.Label(nameFrame, text="Name", bg="white", anchor="w", font=constants.SUB_HEADER).pack(fill="x", expand=True)
  tk.Label(priceFrame, text="Price", bg="white", anchor="w", font=constants.SUB_HEADER).pack(fill="x", expand=True)

  # Loop through the cart / basket and display the item
  for item in basket.values():
    # Item name
    tk.Label(nameFrame, text=str(f"{item['name']}"), bg="white", anchor="w").pack(fill="x", expand=True)
    # Item price * amount
    amountPaid = round(item['amount'] * float(item['price']), 2)
    tk.Label(priceFrame, text=str(f"${amountPaid} (x{item['amount']})"), bg="white", anchor="w").pack(fill="x", expand=True)

  # Subtotal
  tk.Label(nameFrame, text="Subtotal", bg="white", anchor="w").pack(fill="x", expand=True, pady=(12, 0))
  tk.Label(priceFrame, text=str(f"${round(subtotal, 2)}"), bg="white", anchor="w").pack(fill="x", expand=True, pady=(8, 0))

  # Total
  tk.Label(nameFrame, text="Total", bg="white", anchor="w", font=constants.SUB_HEADER).pack(fill="x", expand=True, pady=(12, 0))
  tk.Label(
    priceFrame,
    text=str(f"${round(subtotal, 2)}"),
    bg="white",
    anchor="w"
  ).pack(fill="x", expand=True, pady=(12, 0))

  # Pay with card method
  def payWithCard():
    success = finishAndPay(c, c.coinBalance.get(), "card")
    newWindow.destroy()
    newWindow.update()

  # Pay with cash method
  def payWithCash():
    charge = round(subtotal, 2)
    c.screenMessage.set(f"Please Insert Cash\n${str(charge)}")
    c.stage = screen.PAY_CASH
    newWindow.destroy()
    newWindow.update()

  tk.Label(newWindow, text="Select Payment Method", bg="white", font="Helvetica 10 bold").pack(fill="x", pady=(20, 0))

  # Cash payment button
  tk.Button(
    newWindow,
    command=payWithCash,
    bg=constants.CASH_PURCHASE_BUTTON_BG,
    activebackground=constants.CASH_PURCHASE_BUTTON_HOVER,
    fg=constants.BUTTON_LABEL,
    activeforeground=constants.BUTTON_LABEL,
    text="Insert Cash Manually",
    image=payCashIcon,
    font=constants.COPY_FONT,
    compound="left",
    cursor="hand1",
    bd=0,
    relief="flat",
    borderwidth=0,
    pady=8,
    padx=10
  ).pack(fill="x", pady=(0, 5))

  # Card payment button
  tk.Button(
    newWindow,
    command=payWithCard,
    bg=constants.CARD_PURCHASE_BUTTON_BG,
    activebackground=constants.CARD_PURCHASE_BUTTON_HOVER,
    fg=constants.BUTTON_LABEL,
    activeforeground=constants.BUTTON_LABEL,
    text="Pay with Credit Card",
    image=payCardIcon,
    font=constants.COPY_FONT,
    compound="left",
    cursor="hand1",
    bd=0,
    relief="flat",
    borderwidth=0,
    pady=8,
    padx=10
  ).pack(fill="x")

  newWindow.transient(parent)
  newWindow.grab_set()
