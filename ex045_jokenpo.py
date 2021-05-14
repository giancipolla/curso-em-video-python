from random import randint
intes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Escolha uma opção: \n [0] Pedra, \n [1] Papel, \n [2] Tesoura \n '))
print('-' * 25)
print(f'O jogador escolheu {intes[jogador]}')
print(f'O computador escolheu {intes[computador]}')
print('-' * 25)
if computador == 0: #PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('O jogador ganhou')
    elif jogador == 2:
        print('O jogador perdeu')
    else:
        print('ERRO')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('O jogador perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('O jogador ganhou')
    else:
        print('ERRO')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('O jogador ganhou')
    elif jogador == 1:
        print('O jogador perdeu')
    elif jogador == 2:
        print('Empate')
    else:
        print('ERRO')

















