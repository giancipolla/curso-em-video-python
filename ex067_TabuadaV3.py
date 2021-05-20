while True:
    n = int(input('Escolha um número para saber sua tabuada (digite um valor negativo para sair): '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Obrigado, volte sempre!')




