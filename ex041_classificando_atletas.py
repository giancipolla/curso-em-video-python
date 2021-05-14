from datetime import date
nascimento = int(input('Qual o ano de nascimento? '))
idade = date.today().year - nascimento
if idade <= 9:
    print('O atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta é INFANTIL')
elif idade > 14 and idade <= 19:
    print('O atleta é JUNIOR')
elif idade > 19 and idade <= 25:
    print('O altelta é SENIOR')
else:
    print('O atleta é MASTER')
