#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep #parece que o pc fica pensando...
numPC = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == numPC:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Não foi dessa vez, eu pensei no número {} e não no número {}. Boa sorte na proxima!'.format(numPC, numero))
print('Fim do Jogo')

