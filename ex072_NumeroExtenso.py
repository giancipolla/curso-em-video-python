numeros = ('zero', 'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatroze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    escolha = int(input('Escolha um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Digite um valor válido')
print(f'O número escolhido foi {numeros[escolha]}')


