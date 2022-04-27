#!/usr/bin/env python3
import socket
import pickle
#import tkinter as tk
#from main import Controller
#import components.keypad
from tinydb import TinyDB
from datetime import datetime, date
#from tinydb.operations import increment
from configs.constants import PORT, HOST
#from windows.cart import basket
#from connector import finishAndPay




productDB    = TinyDB("database/product.json")
accountDB    = TinyDB("database/account.json")
transactionDB = TinyDB("database/transaction.json")
machineID    = 100001,

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
socket_client, (host, port) = server.accept()
print(f'Server is running on port {PORT}')



while True:
  data = socket_client.recv(1024)
  if not data: break
  response = pickle.loads(data)

  if response["type"] == "createTransaction":
    balance = response["balance"]
    subtotal = response["subtotal"]
    cart = response["cart"]
    paymentType = response["paymentType"]
    #error = response["Transaction Failed"]

    subtotal = subtotal

    # Calculate the new card payment balance and return the changes if payment method is cash.
    newBalance = balance - subtotal

    # Proceed if user has enough money
    if subtotal <= balance:
      # Decrement stock
      for product in cart.values():
        productDB.update({
          "quantity": product["quantity"] - product["amount"]
        }, doc_ids=[product["id"]])

      # Update Balance
      if paymentType == "card":
        accountDB.update({ "balance": round(newBalance, 2) }, doc_ids=[1])

      # Log trasaction
      transactionID = transactionDB.insert({
        "machineID": machineID,
        "timestamp": str(date.today()),
        "product": product["name"],
        "quantity": product["amount"],
        "subtotal": round(response["subtotal"], 2),
      })

      socket_client.send(pickle.dumps({
        "success": True,
        "balance": round(newBalance, 2),
        "products": productDB.all(),
        "transactionID": transactionID
      }))
    else:
      socket_client.send(pickle.dumps({
        "success": False,
        "message": "Not Enough\nMoney"
      }))

  if response["type"] == "getInventory":
    products = productDB.all()

    labels  = []
    sizes   = []
    colors  = []

    # arguments required for matlibplot library 
    # When the stock is low, it is red; when it is moderately low, it is orange; and when the stock is under control, it is green.
    for product in productDB:
      labels.append(product["name"])
      sizes.append(product["quantity"])
      if product["quantity"] < 10:
        colors.append("red")
      elif product["quantity"] in range(10, 20):
        colors.append("orange")
      else:
        colors.append("#55b70b")

    data = {}
    if products:
      data = {
        "success": True,
        "message": None,
        "labels": tuple(labels),
        "sizes": sizes,
        "colors": colors
      }
    else:
      data = {
        "success": False,
        "message": "Can't fetch inventory",
        "labels": labels,
        "sizes": sizes,
        "colors": colors
      }
    socket_client.send(pickle.dumps(data))

  if response["type"] == "updateAccountBalance":
    success = accountDB.update({"balance": round(response["newBalance"], 2)}, doc_ids=[1])
    socket_client.send(pickle.dumps({ "success": True if success else False }))


