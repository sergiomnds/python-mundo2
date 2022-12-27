
#? Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário
#? digitar 999. No final, mostrar quantos números foram digitados e qual a soma entre eles.

numero = int(input('Digite um número inteiro (999 para parar):'))
contador = 0
soma = 0
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número inteiro (999 para parar):'))
print(f'Contagem: {contador}, Soma: {soma}')
