
#? Escreva um programa em Python que leia um número inteiro qualquer 
#? e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite o número para ser convertido: '))
opcao = int(input('''ESCOLHA PARA QUAL BASE ELE SERÁ CONVERTIDO
        1 - Binário
        2 - Octal
        3 - Hexadecimal
        \nDigite sua opção: '''))

if opcao == 1:
    print('{} em binário é igual a {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em octal é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} em hexadecimal é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
