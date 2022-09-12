
#? Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número inteiro: '))
print('{}'.format('-'*15))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))
print('{}'.format('-'*15))
