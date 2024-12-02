# Shamelessly stolen from:
# https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python

print("\033[1mHello, World!\033[0m") 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.RED + 'Hello, World!' + color.END)    