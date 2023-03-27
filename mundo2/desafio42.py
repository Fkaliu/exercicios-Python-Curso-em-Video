#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: (EQUILÁTERO: todos os lados iguais | ISÓSCELES: dois lados iguais, um diferente | ESCALENO: todos os lados diferente)
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triângulo!')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')
