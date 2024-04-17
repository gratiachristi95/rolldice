# Import needed Modules
import random, os
from subprocess import call

# Define Dice Rolling Function
def rolldice():
  x = random.randint(1,6)
  if x == 6:
      altcodes = [0xE2, 0x9A, 0x85]
      print(bytes(altcodes).decode("utf-8"))
  elif x == 5:
      altcodes = [0xE2, 0x9A, 0x84]
      print(bytes(altcodes).decode("utf-8"))
  elif x == 4:
      altcodes = [0xE2, 0x9A, 0x83]
      print(bytes(altcodes).decode("utf-8"))
  elif x == 3:
      altcodes = [0xE2, 0x9A, 0x82]
      print(bytes(altcodes).decode("utf-8"))
  elif x == 2:
      altcodes = [0xE2, 0x9A, 0x81]
      print(bytes(altcodes).decode("utf-8"))
  else:
      altcodes = [0xE2, 0x9A, 0x80]
      print(bytes(altcodes).decode("utf-8"))

# Define clear function
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# Defines the variable if the user want to roll again
answer = "True"

# While loop to keep the function going until the user exits
while answer == "True":
  # Prompt user input
  n = input("How many dice?\n ")
  n = int(n)

  # Clear Screen
  clear()

  # Rolls the number of dice user inputed
  while n > 0:
    rolldice()
    n = n - 1
    
  answer = input("Would you like to roll again? (True/False)\n")

  clear()
