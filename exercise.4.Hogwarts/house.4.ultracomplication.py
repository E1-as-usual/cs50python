

#definim programul principal, care se ocupa tehnic de sortare
def main(a):
    match a:
        case "Harry" | "Hermione" | "Ron":
            gryf(a)
        case "Draco":
            slyth(a)
        case _:
            backup()

#definim programul de raspuns pentru Gryffindor
def gryf(b):
    print(f"Very good, {b}! After careful consideration, you have been assigned to Gryffindor. \n \
If you have any complaints, don't.")

#definim programul de raspuns pentru Slytherin
def slyth(c):
    print(f"Huh-huh! It appears that you are very nasty, {c}! Well, then, I guess we don't have \
any choice but to send you to Slytherin, where all the dreams go to die. Sorry not sorry.")

#definim programul de backup, care ar trebui sa nu jigneasca prea tare pe cine nu a fost luat in calcul
def backup():
    aa = input("Sorry, I didn't quite catch that. Could you perhaps insert your first and last name? \nMy name is ").strip().title()
    ab , ac = aa.split(" ")
    print(f"Well, I am sorry, little {ab}... It appears that there is no record of any {ac} family in my ledger \n\
of kids that should be expected at Hogwarts. Perhaps you are either a filthy mudblood or a fraud.")
    ba = input("Any comments? \n").strip().capitalize()
    print(f"Did you really just said '{ba}'? That is plain stupid, not even mudblood-level stupid. \n\
Sorry, I would love to carry on the conversation, but, well, I'm lying and I really don't, \
{ab}y or whatever your name was. \n\
Feel free to get your ugly face out of our property. Byee!!")
    

# Acum vrem sa obtinem efectiv numele persoanei si sa rulam main
name = input("Hello, there! Welcome to Hogwarts! I am a strange hat, and you are...? \nMy name is ").strip().title()

main(name)

