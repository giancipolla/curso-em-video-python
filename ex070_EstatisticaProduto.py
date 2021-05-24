total = totmil = menor = cont = 0
barato =' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
#esse bloco abaixo diz que o menor preço inicial sempre será o preço do primeiro produto
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    adicionar = ' '
    while adicionar not in 'SsNn':
        adicionar = str(input('Deseja adicionar mais um produto? [S/N]')).strip().upper()[0]
    if adicionar == 'N':
        break
print(f'O gasto total da compra foi de R$ {total:.2f}')
print(f'{totmil} produtos custam mais de R$ 1.000,00')
print(f'O produto mais barato é: {barato} e ele custa R$ {menor}')








