salario = int(input('Qual o salário atual? '))
if salario > 1250:
    sn = ((salario * 10) / 100) + salario #calculo percentual do salário novo
    print(f'O novo salário será R${sn:.2f}')
else:
    sn = ((salario * 15) / 100) + salario
    print(f'O salário novo será R$ {sn:.2f}')





