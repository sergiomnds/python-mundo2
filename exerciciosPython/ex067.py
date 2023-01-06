
#? Faça um programa que mostre a tabuada de vários números, um de cada vez,
#? para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    try:
        numero = int(input('Quer ver a tabuada de qual valor? '))
        if numero < 0:
            break
        for tabuada in range(1, 11):
            multiplicacao = numero * tabuada
            print(f'{numero} X {tabuada} = {multiplicacao}')
    except ValueError:
        print('Valor Inválido')
print('Volte Sempre!')
    