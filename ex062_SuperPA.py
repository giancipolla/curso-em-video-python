primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razão
        cont += 1
    mais = int(input('Quantos termos você deseja adicionar? '))




