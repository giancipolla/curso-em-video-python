total = 0
numero = int(input('Informe um número '))
for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1
if total == 2:
    print('O número é primo')
else:
    print('O número não é primo')








