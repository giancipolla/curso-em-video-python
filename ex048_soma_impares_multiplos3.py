soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c #nessa condição, a soma recebe 0 + todos os números múltiplos de 3
        cont = cont + 1 #esse contado está verificando quantos números existem na condição determinada
print(f'A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é {soma}, e existem {cont} números nessa condição')











