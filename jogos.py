from random import randint

randList = randint(0, 10000)
str(randList)
jogo = []
lista = []

for x in range(10):
    for y in range (6):
        lista.append(randint(0, 60))
    jogo.append(lista[:])
    lista.clear()
       


arquivo = open(f"jogos{randList}.txt", "w")
for l in jogo:
    arquivo.write(str(l) + "\n")
    
arquivo.close()
