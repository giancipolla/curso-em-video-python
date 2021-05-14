vc = float(input('Qual o valor da casa a ser adquirida? R$ '))
s = float(input('Qual o salário do comprador? R$ '))
tempo = int(input('Em quantos anos o imóvel será parcelado? '))
prest = vc / (tempo * 12)
pm = (30 * s) / 100 #prestação máxima
if prest > pm:
    print('\033[1;31mInfelizmente o financiamento não será aprovado\033[m')
    quit()
elif prest <= s:
    print(f'O financiamento será aprovado. A quitação será em {tempo} anos, e a parcela será de R${prest:.2f}.')
print('Obrigado por comprar conosco!')








