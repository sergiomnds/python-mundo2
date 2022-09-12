'''for c in range (1, 10):
    print(c)
print('Fim')'''

contador = 1
while contador < 10:
    print(contador)
    contador += 1
print('Fim')

resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares.")
