import math
import random
n = int(input('Escolha um número de 0 a 10: '))
lista = [1,2,3,4,5,6,7,8,9,10]
escolhapc = random.choice(lista)
tentativas = 1
while n is not escolhapc:
    n = int(input('Tente novamente: '))
    tentativas += 1
print(f'Você acertou na {tentativas}ª tentativa!')













