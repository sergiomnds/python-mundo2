
#? Crie um programa que leia vários nºs inteiros. No final, mostra a média e qual foi o maior e menor
#? valor lido. O programa deve perguntar se ele quer ou não continuar a digitar os valores.

resposta = "S"
soma = 0
contador = 0
maior = 0
menor = 0

while resposta in "S":
    numero = int(input('Digite um valor inteiro:'))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? (S/N)')).upper().strip()[0]
media = soma/contador
print(f'Você digitou {contador} números e a média foi {media}! \nMaior nº: {maior} \nMenor nº: {menor}')
