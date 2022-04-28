# Stages
CODE    = 1
AMOUNT  = 2
CONFIRM = 3
PAY_CASH = 4

# Buttons
HELP = "HELP"
CLEAR   = "CLR"

BUTTONS = [
  ["A", "1", "2", "3"],
  ["B", "4", "5", "6"],
  ["C", "7", "8", "9"],
  [HELP, ".", "0", CLEAR]
]

# Button code combinations
BUTTON_CODES = { "A1": 0, "A2": 1, "A3": 2, "B1": 3, "B2": 4}
PRODUCT_CODES = { 1: "A1", 2: "A2", 3: "A3", 4: "B1", 5: "B2"}
