
#Importam utilitatile necesare
import sys

# Verificam dimensiunea inputului
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

#Odata ce am verificat inputul ne ocupam de restul programului
print ("Hello, my name is", sys.argv[1]) 
