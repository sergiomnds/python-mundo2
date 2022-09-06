for c in range(0,6): #* Imprime 6 vezes, não conta o ultimo numero. DE 0 A 5
    print('Oi')
    
for c in range (6, 0, -1): #* Conta de trás pra frente. Precisa do -1 para dizer como vai ser a contagem.
    print(c)
#!Saída:
#! 6
#! 5
#! 4
#! 3
#! 2
#! 1

for c in range (0, 7, 2): #* Conta de 2 em 2.
    print(c)
    
n = int(input('Digite um número: '))
for c in range(0, n + 1): #* '+1' para contar o numero digitado.
    print(c)
    
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim + 1, passo):
    print(c)

soma = 0 #*Declaração fora do loop.
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    soma = soma + n
print('O somatório de todos os valores foi {}'.format(soma))