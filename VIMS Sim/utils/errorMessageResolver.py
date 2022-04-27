# pyright: reportMissingImports=false
import configs.screen as screen
from utils.loader import blink

# This procedure is called if an error occurs. For instance, an out-of-stock error,
# an  number error, or a button error.
def errorMessageResolver(c, message):
  subtotal = c.subtotal.get()
  charge = round(subtotal, 2)
  blink(c, message)
  if c.stage == screen.CODE: c.screenMessage.set("Enter Item Code")
  if c.stage == screen.AMOUNT: c.screenMessage.set("Enter Quantity")
  if c.stage == screen.PAY_CASH: c.screenMessage.set(f"Please Insert Cash\n${str(charge)}")
