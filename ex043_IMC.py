p = float(input('Digite seu peso em kg '))
a = float(input('Digite sua altura '))
imc = p / (a ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está: Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está: Com peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está: Com Sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.2f} e você está: Com Obesidade')
else:
    print(f'Seu IMC é {imc:.2f} seu status é: Com Obesidade Mórbida')



