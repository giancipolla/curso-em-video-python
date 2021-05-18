resp = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'A Média dos valores digitados é {soma / cont}, o maior número é {maior} e o menor número é {menor}')









