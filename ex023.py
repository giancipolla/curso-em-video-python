numero = int(input('Digite um número '))
u = numero // 1 % 10
c = numero // 10 % 10
d = numero // 100 % 10
m = numero // 1000 % 10
print(f'A unidade é {u}')
print(f'A centena é {c}')
print(f'A dezena é {d}')
print(f'O milhar é {m}')
