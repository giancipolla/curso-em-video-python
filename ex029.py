velocidade = float(input('Qual a velocidade? '))
vm = 80 #velocidade máxima permitida
ve = velocidade - vm #velocidade excedida
multa = ve * 7
if velocidade <= vm:
    print('Não haverá multa')
else:
    print(f'Você será multado em {multa:.2f}')




