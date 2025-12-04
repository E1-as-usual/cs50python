

#pentru inceput creem variabila name, care va primi input-ul

name = input("What is your name?")


#In continuare, creem variabila file, care primeste valoarea returnata de unctia open

file = open("names.txt", "w")

file.write(name)

file.close()

