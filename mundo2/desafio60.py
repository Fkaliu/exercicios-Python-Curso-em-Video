#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n1 = int(input('Digite um numero para calcular seu Fatorial: '))
resultado = 1
cont = n1
print('Calculando {}!'.format(n1, end=''))
while cont > 0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else '= ', end='')
    resultado *= cont
    cont -= 1
print('{}'.format(resultado))
