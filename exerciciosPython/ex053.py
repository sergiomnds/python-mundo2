
#? Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
fraseAnalise = ''.join((frase.split()))
inverso = ''
for letra in range(len(fraseAnalise) - 1, -1, -1):
    inverso += fraseAnalise[letra]
print('O inverso de {} é {}'.format(fraseAnalise, inverso))
if(inverso == fraseAnalise):
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')