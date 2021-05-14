nome = str(input('Digite seu nome completo ')).strip()
print(f'O nome em maiusculo é {nome.upper()}')
print(f'O nome em minúsculo é {nome.lower()}')
print(f'O nome tem {len(nome) - nome.count(" ")} letras')
primeiro = nome.split()
print(f'O primeiro nome tem {len(primeiro[0])} letras')


















