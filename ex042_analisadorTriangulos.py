l1 = int(input('Digite o lado 1 '))
l2 = int(input('Digite o lado 2 '))
l3 = int(input('Digite o lado 3 '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: #verifica se os lados podem formar um triangulo
    print('Os lados formam um triangulo')
    if l1 == l2 == l3:
        print('O triangulo Equilátero')
    elif l1 != l2 != l3 and l1 != l3:
        print('O triangulo é escaleno')
    else:
        print('O triangulo é isósceles')
else:
    print('Os lados não podem formar um triângulo')










