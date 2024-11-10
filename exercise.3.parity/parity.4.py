'''Acest program NU este cea mai simpla si eficienta varianta a codului, varianta respectiva este parity.0.0.py'''


# definim functia principala, care se ocupa de suprafata programului
def main(a):
    if is_even(a):
        printparity( a , ending = "even" )
    else:
        printparity( a , ending = "odd" )

# definim functia care verifica paritatea
def is_even(b):
    return b % 2 == 0 

# definim functia care printeaza textul in functie de ce avem nevoie
def printparity( c , ending = "" ):
    print( f"The number you have chosen ( {c} ) is " , end = "" , sep = "" )
    print( f"{ending}.")

x = int(input("Introduceti numarul dorit: X = "))    
main(x)

    
    
