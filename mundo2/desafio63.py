#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('{}'.format('-'*30))
print('Sequencia de Fibonacci')
print('{}'.format('-'*30))
termo = int(input('Quantos termos vc quer mostrar? '))
n1 = 0
n2 = 1
print('{}'.format('-'*30))
print('{} {}'.format(n1, n2), end='')
c = 3
while c <= termo:
    fibo = n1 + n2
    print(' {}'.format(fibo), end='')
    n1 = n2
    n2 = fibo
    c += 1
print(' Fim')
