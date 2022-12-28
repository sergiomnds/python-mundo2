
#! While infinito!
cont = 1
while cont <= 10: #* SE USAR 'True fica infinito!
    print(cont, '-> ', end='')
    cont += 1
print('Acabou!')

cont = 1
while True: 
    print(cont, '-> ', end='')
    cont += 1
print('Acabou!') #* Até fica transparente o código, porque ele não vai ser feito realmente.

#? O loop infinito vai ser utilizado com o 'break' para whiles com Flag.
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')