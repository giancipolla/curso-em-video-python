produtos = ('Celular', 1500.00, 'Computador', 5000.00, 'SmartWatch', 3400.00)
for pos in range(0, len(produtos)): #o range começa na posição 0 e vai até o tamanho da lista de produtos
    if pos % 2 == 0: #se a posição for par, exibe o elemento da posição que está nos pares, ou seja, os nomes dos produtos
        print(f'{produtos[pos]:.<30}', end='')
    else: #se a posição for ímpar, exibe quem está nas posições ímpares, ou seja, os preços
        print(f'R$ {produtos[pos]:.2f}')


