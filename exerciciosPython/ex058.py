
#? Melhore o jogo do Desafio 028 onde o computador vai “pensar” em um número entre 0 e 10.
#? O jogador vai tentar adivinhar até acertar, mostrando no final
#? quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

sorteado = randint(0, 10)
escolhido = int(input('Diga qual número acha que o computador pensou: '))
sleep(2) #! Função que faz o terminal esperar 'x'(2) segundos até aparecer o resultado.

tentativas = int(0)
while sorteado != escolhido:
    tentativas += 1
    if escolhido < sorteado:
        print('O número pensado é maior! Tente novamente!')
    elif escolhido > sorteado:
        print('O número pensado é menor! Tente novamente!')
    escolhido = int(input('Diga qual número acha que o computador pensou: '))
    sleep(2)

if sorteado == escolhido:
    print('Parabéns! Você adivinhou!')
    print(f'Você precisou de {tentativas} tentativas para acertar.')
    