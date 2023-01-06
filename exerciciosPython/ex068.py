
#? Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#? mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

contador = 0
while True:
    jogador = int(input('Escolha um valor inteiro: '))
    computador = randint(0,5)
    total = computador + jogador
    aposta = int(input('1- Par \n2- Ímpar \nVai dar par ou ímpar? '))
    if aposta == 1:
        if total % 2 == 0:
            print(f'Parabéns! \nVocê apostou par e o valor deu {total}')
            contador +=1
        else:
            print('Não foi dessa vez!')
            break
    elif aposta == 2:
        if total % 2 != 0:
            print(f'Parabéns! \nVocê apostou ímpar e o valor deu {total}')
            contador +=1
        else:
            print('Não foi dessa vez!')
            break
    print('Vamos novamente...')
print(f'Mais sorte na próxima! \nVocê venceu o computador {contador} vezes seguidas!')
    