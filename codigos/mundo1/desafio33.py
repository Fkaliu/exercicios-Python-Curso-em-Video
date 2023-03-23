#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
#menor numero
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor número é {:.0f}'.format(menor))
#maior numero
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {:.0f}'.format(maior))

