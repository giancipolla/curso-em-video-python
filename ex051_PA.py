primeiro = int(input('Digite o primeiro número da sequência '))
razão = int(input('Digite a razão da sequência '))
décimo = primeiro + (10 - 1) * razão #formula pra calcular o quantos numeros esta PA terá. numero = primeiro (numero -1) * razao
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' ')






