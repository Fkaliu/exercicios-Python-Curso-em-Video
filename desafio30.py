#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Me diga um numero qualquer: '))
if (numero % 2) == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
