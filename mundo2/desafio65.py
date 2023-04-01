#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma = qtdd = media = 0
maior = menor = 0
while resp in 'S':
    numero = float(input('Digite um número: '))
    soma += numero
    qtdd += 1
    if qtdd == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()
media = soma/qtdd
print('Você digitou {} numeros e a média foi {}'.format(qtdd, media))
print('O maior valor digitado foi {} e o menor valor foi {}'.format(maior, menor))
