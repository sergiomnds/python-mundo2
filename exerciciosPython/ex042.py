
#? Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#? – EQUILÁTERO: todos os lados iguais
#? – ISÓSCELES: dois lados iguais, um diferente
#? – ESCALENO: todos os lados diferentes

a = int(input('Escreva o valor da 1º reta: '))
b = int(input('Escreva o valor da 2º reta: '))
c = int(input('Escreva o valor da 3º reta: '))

if abs(b - c) < a and a < (b + c) and abs(a - c) < b and b < (a + c) and abs(a - b) < c and c < (a + b):
    print('Elas podem formar um triângulo!')
    if a == b == c:
        print('O triângulo será Equilátero!')
    elif a == b or a == c or b == c:
        print('O triângulo será Isósceles!')
    else:
        print('O triângulo será Escaleno!')
else:
    print('As retas não formam um triângulo!')
