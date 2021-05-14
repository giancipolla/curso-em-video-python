preço = float(input('Digite o preço do produto R$ '))
cond = str(input('Qual a condição do pagamento? \n Digite: '
                 '\n A para dinheiro,'
                 '\n B para pagamento a vista no cartão, '
                 '\n C para pagamento em até 2x no cartão '
                 '\n D para pagamento em 3x ou mais no cartão '
                 '\n ')).strip().capitalize()
if cond == 'A':
    print(f'Preço a pagar será: R$ {preço - (preço * 10) / 100:.2f}')
elif cond == 'B':
    print(f'Preço a pagar será: R$ {preço - (preço * 5) / 100:.2f}')
elif cond == 'C':
    print(f'Preço a pagar será: R$ {preço:.2f}, em duas parcelas de R$ {preço / 2:.2f}')
elif cond == 'D':
    pc = preço + (preço * 20) / 100  # preço de compra final
    parcela = int(input('Informe o número de parcelas '))
    if parcela > 10 or parcela < 3:
        print('ERRO: O valor pode ser parcelado entre 3x e 10x')
        quit()
    vp = pc / parcela #valor da parcela
    print(f'O valor final da compra será R$ {pc:.2f} em {parcela}x de R$ {vp:.2f}')





















