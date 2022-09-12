
# ? Crie um programa que leia o ano de nascimento de sete pessoas.
# ? No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
contMaior = 0
contMenor = 0
ANO_ATUAL = 2022
for c in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    if ANO_ATUAL - ano >= 18:
        contMaior += 1
    else:
        contMenor += 1
print(f"{contMaior} pessoas são maiores de idade e {contMenor} são menores de idade.")
