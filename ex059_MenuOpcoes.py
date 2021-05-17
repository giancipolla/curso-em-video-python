v1 = int(input('Digite o primeiro valor '))
v2 = int(input('Digite o segundo valor '))
comando = 0
while comando != '5':
    comando = str(input('''O que deseja fazer com os valores: 
    [1] Somar  
    [2] Multiplicar 
    [3] Maior  
    [4] Novos Números 
    [5] Sair 
     '''))
    if comando == '1':
        print(f'A soma de {v1} + {v2} é igual a {v1 + v2}')
    elif comando == '2':
        print(f'A multiplicação de {v1} por {v2} é {v1 * v2}')
    elif comando == '3':
        if v1 > v2:
            print(f'O maior número é {v1}')
        else:
            print(f'O maior número é {v2}')
    elif comando == '4':
        v1 = int(input('Digite um novo número '))
        v2 = int(input('Digite outro novo número '))
    elif comando == '5':
        print('Até a próxima!')
        quit()
    else:
        print('Opção Inválida')
    print('=-=' * 10)









