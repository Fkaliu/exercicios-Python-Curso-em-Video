#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o angulo que vc deseja: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O angulo de {} tem o SENO de {:.2f}'.format(a, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, tg))
