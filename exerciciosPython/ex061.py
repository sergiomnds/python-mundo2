
#? Refaça o desafio 051, lendo o primeiro termo e a razão de um PA
#? mostrando os 10 primeiros termos da progressão usando While.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0

print(f'{termo} -> ', end= '')
while contador < 10:
    termo += razao
    contador += 1
    print(f'{termo} -> ' if contador != 10 else f'{termo}', end='')