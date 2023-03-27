#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
a = 'PEDRA'
b = 'PAPEL'
c = 'TESOURA'
lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaPC = random.choice(lista)
print('Suas opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
escolha = int(input('Qual é a sua jogada? '))
if escolha == 0:
    print('Opção INVALIDA. Tente novamente')
elif escolha >=4:
    print('Opção INVALIDA. Tente novamente')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    print('=-=' * 20)
    print('Computador jogou {}'.format(escolhaPC))
    if escolha == 1:
        escolha = 'PEDRA'
        print('Jogador jogou {}'.format(a))
    elif escolha == 2:
        escolha = b
        print('Jogador jogou {}'.format(b))
    elif escolha == 3:
        escolha = c
        print('Jogador jogou {}'.format(c))
    print('=-=' * 20)
    if escolha == escolhaPC:
        print('EMPATE')
    elif escolhaPC == 'PEDRA' and escolha == b:
        print('Computador PERDEU')
    elif escolhaPC == 'PEDRA' and escolha == c:
        print('Computador VENCEU')
    elif escolhaPC == 'PAPEL' and escolha == a:
        print('Computador VENCEU')
    elif escolhaPC == 'PAPEL' and escolha == c:
        print('Computador PERDEU')
    elif escolhaPC == 'TESOURA' and escolha == a:
        print('Computador PERDEU')
    elif escolhaPC == 'TESOURA' and escolha == b:
        print('Computador VENCEU')
