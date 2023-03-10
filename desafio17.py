#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (ca ** 2 + co ** 2) ** (1/2)
h1 = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(h))
print('outra forma de calcular a hipotenusa {}'.format(h1))




