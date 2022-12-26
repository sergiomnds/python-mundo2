
#? Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Escreva o nº para calcular fatorial: '))
cont = numero
fatorial = 1

print(f'{numero}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')

    fatorial *= cont
    cont -= 1
print(f'{fatorial}')