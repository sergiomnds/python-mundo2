
#? Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#? Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#? A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o preço da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anosAPagar = float(input('Quantos anos para pagar? '))
meses = anosAPagar * 12
prestacao = valorCasa / meses

if prestacao > (0.3 * salario): #* 30% do salário
    print('O valor da prestação excede 30% do Salário! \nNão foi possível aprovar o empréstimo!')
else:
    print('O empréstimo está aprovado! Atende aos requisitos necessários.')
    