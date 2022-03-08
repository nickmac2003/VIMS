import pickle
import socket
import threading
from time import sleep
import configs.screen as screen
from configs.constants import PORT, HOST
from utils.typewriter import typerwriter
from utils.loader import loading, blink
from utils.playSound import playSoundEffect

# This file serves as a middleman for the client and the server. It handles all
# requests sent from the client to the server or the other way around.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Transaction Failed Messages
def onError(c, message):
  blink(c, message)
  typerwriter(c, ["Transaction Failed"])

# Good bye messages
def goodbye(c):
  messages = ["Thank you.", "Rock Chalk, Jayhawk!"]
  typerwriter(c, messages)
  c.stage = screen.CODE

def processPayment(c, newBalance, paymentMethod):
  loading(c)
  sleep(0.5)
  if paymentMethod == "card":
    c.coinBalance.set(round(newBalance, 2))
  c.screenMessage.set("\u2713 Paid \u2713")
  playSoundEffect(5)
  sleep(2)
  # If payment method is cash, return changes
  if paymentMethod == "cash":
    c.screenMessage.set(str(f"Change: ${round(newBalance, 2)}"))
    sleep(2)
    c.screenMessage.set("")
    blink(c, str(f"Change: ${round(newBalance, 2)}"))

  c.screenMessage.set("")
  threading.Thread(target=goodbye, args=(c,)).start()

# Handle transactions, calculate changes and update account balance 
def finishAndPay(c, balance, paymentMethod):
  subtotal = c.subtotal.get()
  client_socket.send(pickle.dumps({
    "type": "createTransaction",
    "cart": c.basket,
    "balance": balance,
    "subtotal": float(subtotal),
    "paymentType": paymentMethod
  }))

  data = client_socket.recv(1024)
  response = pickle.loads(data)

  # Result transaction state
  c.basket = {}
  c.subtotal.set(0)
  c.cart.set(0)


  # If the server request is successful, the client should be updated.
  if response["success"] == True:
    for index, product in enumerate(response["products"]):
      c.products[index].quantity.set(product["quantity"])

    # If payment is successful, let user know and print message on screen
    threading.Thread(target=processPayment, args=(c, response["balance"], paymentMethod,)).start()
    playSoundEffect(6)
    return True
  else:
    # If errors did occur. Display message on screen
    threading.Thread(target=onError, args=(c, response["message"],)).start()
    playSoundEffect(4)
    c.stage = screen.CODE
    return False

# GET request for inventory
def getInventory():
  pickle_object = pickle.dumps({ "type": "getInventory" })
  client_socket.send(pickle_object)

  data = client_socket.recv(1024)
  response = pickle.loads(data)
  return response

# Update account balance
def updateAccountBalance(c, newBalance):
  pickle_object = pickle.dumps({
    "type": "updateAccountBalance",
    "newBalance": newBalance
  })
  client_socket.send(pickle_object)

  data = client_socket.recv(1024)
  response = pickle.loads(data)
  if response["success"]:
    c.coinBalance.set(round(newBalance, 2))
  return response