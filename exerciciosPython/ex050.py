
#? Desenvolva um programa que leia seis números inteiros
#? e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {}º número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\nVocê informou {} números pares.'.format(cont))
print('A soma dos números pares é {}.'.format(soma))
