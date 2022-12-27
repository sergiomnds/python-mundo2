
#? Crie um programa que leia vários nºs inteiros. No final, mostra a média e qual foi o maior e menor
#? número valores lidos. O programa deve perguntar se ele quer ou não continuar a digitar os valores.

numero = int(input('Digite um valor inteiro:'))
contador = 0
soma = 0
maior = 0
menor = numero

resposta = str(input('Deseja continuar? (S/N)')).upper()
while resposta == 'S':
    contador += 1
    soma += numero
    media = soma/contador
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    resposta = str(input('Deseja continuar? (S/N)')).upper()

print(f'''Contagem de Números: {contador}
        Média dos valores: {media}
        Maior valor: {maior}
        Menor Valor: {menor}''')
