viagem = int(input('Quantos km terá a viagem? '))
if viagem <= 200:
    print(f'Sua viagem custará {viagem * 0.5:.2f} reais')
elif viagem > 200:
    print(f'Sua viagem custará {viagem * 0.45:.2f}')
else:
    print('Sua viagem não pode ter 0km')
print('Você deve digitar um número válido')



