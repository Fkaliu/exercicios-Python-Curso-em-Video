#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(n, math.trunc(n)))
print('O valor inteiro pode ser apresentado de outro modo = {}'.format(int(n)))

