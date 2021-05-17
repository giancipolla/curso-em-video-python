#tira os espaços no final e começo da resposta, coloca em maiusculo e considera só a primeira letra
sexo = str(input('Digite M para Homem e F para mulher ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido! Por favor digite seu sexo: M/F ')).strip().upper()[0]
print(f'Dado registrado com sucesso! O sexo digitado é {sexo}')









