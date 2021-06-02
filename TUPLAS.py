#maneira de exibir essa tupla no print usando FOR
lanche = ('Burger', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi demais!')