x = int(input("Please insert your number. X = "))

def main(a):
    if is_even(a):
        print1( a , ending = "even")
    else:
        print1( a , ending = "odd")
        
def is_even(b):
    if b % 2 == 0:
        return True
    else:
        return False 
    
def print1( c , ending = "" ):
    print( f"The number you have chosen ( {c} ) is " , end = "" , sep = "" )
    print( f"{ending}.")

    
main(x)

    
    
