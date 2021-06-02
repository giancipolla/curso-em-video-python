valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) #assim conseguimos inserir os valores da lista através do teclado
for c, v in enumerate(valores): #o enumerate faz a contagem das keys e podemos usar isso para associar a key a um elemento da lista
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')


