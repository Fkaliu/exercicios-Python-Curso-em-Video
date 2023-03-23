##Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')
else:
    print('Os seguimentos acima PODEM FORMAR um triângulo')