num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),)
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vez(s)')
else:
    print('O número 9 não foi digitado')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
for n in num:
    if n %2 == 0:
        print(f'Os número pares são: {n}')








