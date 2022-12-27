
#? Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
#? mais alguns termos. O programa encerra quando ele disser que mostrar 0 termos.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0

print(f'{termo} -> ', end= '')
while contador < 10:
    termo += razao
    contador += 1
    print(f'{termo} -> ' if contador != 10 else f'{termo}', end='')

contador = int(input('\nQuantos termos você quer a mais?'))
while contador > 0:
    termo += razao
    contador -= 1
    print(f'{termo} -> ' if contador > 0 else f'{termo}', end='')
    if contador == 0:
        contador = int(input('\nQuantos termos você quer a mais?'))

print('FINALIZADO')
