from random import choice
n1 = input('Primeira pessoa ')
n2 = input('Segunda pessoa ')
n3 = input('Terceria pessoa ')
n4 = input('Quarta pessoa ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'Quem vai buscar a comida na portaria é {escolhido}')



