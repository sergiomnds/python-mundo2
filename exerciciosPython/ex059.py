
#? Crie um programa que leia dois valores e mostre um menu na tela:
#? [1] somar
#? [2] multiplicar
#? [3] maior
#? [4] novos números
#? [5] sair do programa
#? Seu programa deverá realizar a operação solicitada em cada caso.

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
sair = False

while sair is not True:
    escolha = int(input('Escolha um valor dentre os valores abaixo:\n1- Somar \n2- Multiplicar \n3- Maior \n4- Novos números \n5- Sair do programa \n'))

    if escolha == 1:
        print(f'{primeiroNumero} + {segundoNumero} = {primeiroNumero + segundoNumero}')

    elif escolha == 2:
        print(f'{primeiroNumero} * {segundoNumero} = {primeiroNumero * segundoNumero}')

    elif escolha == 3:
        if primeiroNumero > segundoNumero:
            print(f'O maior número é {primeiroNumero}!')
        elif primeiroNumero < segundoNumero:
            print(f'O maior número é {segundoNumero}!')
        else:
            print('Os números são iguais!')

    elif escolha == 4:
        primeiroNumero = int(input('Digite o primeiro número: '))
        segundoNumero = int(input('Digite o segundo número: '))

    elif escolha == 5:
        print('Saindo...')
        sair = True
    
    else:
        print('Opção inválida!')
    print('=-=' * 10)
