frase = str(input('Digite a frase ')).strip().upper()
palavras = frase.split() #separa a frase em palavras dentor de uma lista
junto = ''.join(palavras) #junta as palavras deixando-as sem espaço entre elas
inverso = '' #acumulador para juntar as letras do laço e escrever a palavra
for letra in range(len(junto) -1, -1, -1): #laço lê a frase sem espaços de traz pra frente
    inverso += junto[letra] #o contador inverso junto a palavra de trás pra frente
if inverso == junto:
    print('É Palíndromo')
else:
    print('Não é Palíndromo')





