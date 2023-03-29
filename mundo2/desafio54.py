#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for anonasc in range(1, 8):
    anonasc = int(input('Em que ano a {}° pessoa nasceu? '.format(anonasc)))
    if anoatual - anonasc >=18:
        maior += 1
    elif anoatual - anonasc <18:
        menor += 1
print('da lista informada, temos {} maiores de idade e {} menores de idade.'.format(maior, menor))

