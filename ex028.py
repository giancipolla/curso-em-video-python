import math
import random
n = int(input('Escolha um número de 0 a 5 '))
lista = [0, 1, 2, 3, 4, 5]
choice = random.choice(lista)
if n == choice:
    print('Você acertou, parabéns!')
else:
    print('Você errou, tente novamente')






