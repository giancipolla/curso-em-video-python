from datetime import date
TotalIdade = 0
maisvelho = 0
nomemaisvelho = ''
Menos20 = 0
for c in range(1,5):
    print(f'---------{c}ª pessoa---------')
    nome = str(input('Nome ')).strip().upper()
    idade = int(input('Idade '))
    sexo = str(input('Sexo: [M/F] ')).strip()
    TotalIdade += idade
    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if idade > maisvelho and sexo in 'Mn':
            maisvelho = idade
            nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        Menos20 += 1
print(f'A média de idade do grupo é {TotalIdade / 4}')
print(f'O homem mais velho tem {maisvelho} anos e seu nome é {nomemaisvelho}')
print(f'São {Menos20} mulheres com menos de 20 anos no grupo')



















