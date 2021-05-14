from datetime import date
nascimento = int(input('Informe seu ano de nascimento '))
idade = date.today().year - nascimento
if idade < 18:
    print(f'Você precisa se alistar no excército daqui a {18 - idade} anos')
elif idade == 18:
    print('Você deve se alistar esse ano')
else:
    print(f'Já passaram {idade - 18} anos o prazo do seu alistamento')




