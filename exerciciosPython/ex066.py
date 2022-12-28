
#? Leia vários números inteiros. O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
#? No final, mostrar quantos números foram digitados e qual a soma entre eles.
soma = 0
contador = 0
while True:
    try:
        numero = int(input('Informe um número inteiro: '))
        if numero == 999:
            break
        soma += numero
        contador += 1
    except ValueError:
        print('Inválido')

print(f'Você digitou {contador} e a soma vale {soma}')