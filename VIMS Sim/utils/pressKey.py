# pyright: reportMissingImports=false
import threading
import configs.screen as screen
from wrappers.keypad import lockerWrapper 
from windows.help import helpWindow
from utils.playSound import playSoundEffect

# The CLR and digit buttons each have their own sound effects.
getSound = lambda button : playSoundEffect(1) if button == "CLR" else playSoundEffect(2)

@lockerWrapper
def pressKey(c, parent, button):
  subtotal = c.subtotal.get()
  charge = round(subtotal, 2)

  if button == screen.HELP:
    # Open help window
    helpWindow(parent)

  # Clear button pressed
  # When the user clicks the clear button, the screen message is reset
  elif button == screen.CLEAR:
    threading.Thread(target=getSound, args=(button,)).start()
    if c.screenMessage.get() == "Enter Quantity":
      c.screenMessage.set("Enter Item Code")
      c.stage = screen.CODE
    elif c.stage == screen.AMOUNT:
      c.screenMessage.set("Enter Quantity")
    elif c.stage == screen.PAY_CASH:
      c.screenMessage.set(f"Please Insert Cash\n${str(charge)}")
    else:
      c.screenMessage.set("Enter Item Code")
      c.stage = screen.CODE
    c.toggleLock(False)

  # Digit button pressed
  else:
    threading.Thread(target=getSound, args=("",)).start()
    previous = c.screenMessage.get()
    messages = ("Enter Item Code", "Enter Quantity", f"Please Insert Cash\n${str(charge)}")
    if previous in messages:
      c.screenMessage.set(button)
    else:
      c.screenMessage.set((previous + button))
