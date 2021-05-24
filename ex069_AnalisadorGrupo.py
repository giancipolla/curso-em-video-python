idade = 0
sexo = ' '
adicionar = ' '
cont18 = 0
conth = 0
contm20 = 0
while adicionar not in 'N':
    idade = int(input('Digite uma idade: '))
    if idade > 18:
        cont18 += 1
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        conth += 1
    if idade < 20 and sexo == 'F':
        contm20 += 1
    adicionar = str(input('Quer adicionar mais uma pessoa? [S/N] ')).strip().upper()[0]
print(f'Foram cadastradas {cont18} pessoas com mais de 18 anos, {conth} homen(s) e {contm20} mulher(s) com menos de 20 anos')








