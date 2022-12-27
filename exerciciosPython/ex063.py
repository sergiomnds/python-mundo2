
#? Escreva um programa que leia um nº n e mostre na tela os n primeiros
#? elementos de uma sequencia de Fibonacci.
print('SEQUÊNCIA DE FIBONACCI')
qntTermo = int(input('Quantos termos devem ser mostrados? '))
numero = 1
segNumero = 0

while qntTermo > 0:
    tercNumero = numero + segNumero
    print(f'{tercNumero} -> ' if qntTermo != 1 else f'{tercNumero}', end='')
    numero = segNumero
    segNumero = tercNumero
    qntTermo -= 1
print('\nFIM')
