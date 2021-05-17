print('Sequência de Finonacci')
termos = int(input('Quantos termos você quer na sequência? '))
#primeiro termo obrigatório de Fibonacci
t1 = 0
#Segundo termo obrigatório de Fibonacci
t2 = 1
print(f'{t1} - {t2} - ', end='')
#contador começa em 3 pois já temos os 2 primeiros termos
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f'{t3} - ', end="")
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')












