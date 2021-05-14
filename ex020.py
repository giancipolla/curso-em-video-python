from random import shuffle
n1 = input('Digite um nome ')
n2 = input('Digite outro nome ')
n3 = input('Digite outro nome ')
nomes = [n1, n2, n3]
shuffle(nomes)
print('A ordem de apresentação será ')
print(nomes)

