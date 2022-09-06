
#? Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice

print('''Escolha uma das opções abaixo:
      1 - Pedra
      2 - Papel
      3 - Tesoura''')
escolha = int(input("Digite a opção: "))
listaOpcao = ['Pedra', 'Papel', 'Tesoura']
escolhaPC = choice(listaOpcao)

if escolha != 1 and escolha != 2 and escolha != 3:
    print("Opção inválida!")
else:
    if (escolha == 1 and escolhaPC == 'Pedra') or (escolha == 2 and escolhaPC == 'Papel') or (escolha == 3 and escolhaPC == 'Tesoura'):
        print('Empate!')
        print('Você escolheu {} e o PC escolheu {}!'.format(listaOpcao[escolha - 1], escolhaPC))
    elif (escolha == 1 and escolhaPC == 'Tesoura') or (escolha == 2 and escolhaPC == 'Pedra') or (escolha == 3 and escolhaPC == 'Papel'):
        print('Você ganhou!')
        print('Você escolheu {} e o PC escolheu {}!'.format(listaOpcao[escolha - 1], escolhaPC))
    else:
        print('Você perdeu!')
        print('Você escolheu {} e o PC escolheu {}!'.format(listaOpcao[escolha - 1], escolhaPC))
