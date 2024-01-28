from random import randint

randList = randint(0, 10000)
str(randList)
jogo = []
lista = []

input = int(input("Quantos jogos? "))

for x in range(input):
    for y in range (6):
        lista.append(randint(0, 60))
    jogo.append(lista[:])
    lista.clear()
       


arquivo = open(f"jogos{randList}.txt", "w")
for l in range (len(jogo)):
    arquivo.write(str(jogo[l]) + "\n")
    
arquivo.close()
