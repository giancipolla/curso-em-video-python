cont = soma = 0
while True:
    n = int(input('Digite um número, para parar digite 999: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'{cont} números foram digitados e a soma entre eles é {soma}')
