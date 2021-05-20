import random
from random import randint
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'O computador escolheu {computador} e você escolheu {jogador}, o Total é {total}')
    if tipo == 'P':
        if total %2 == 0:
            print('Você venceu')
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você venceu')
        else:
            print('Você perdeu')
            break
























