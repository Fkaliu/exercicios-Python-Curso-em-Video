#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
par = impar = cont = 0
print('{}'.format('-'*40))
print('VAMOS JOGAR PAR OU IMPAR')
print('{}'.format('-'*40))
while True:
    nplayer = int(input('Digite um valor: '))
    nPC = randint(1, 10)
    result = nPC + nplayer
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {nplayer} e o computador {nPC}. Total de {result}')
    print('{}'.format('-'*40))
    if escolha == 'P':
        if result % 2 == 0:
            print('Você VENCEU!')
            print('{}'.format('-' * 40))
            cont += 1
        else:
            print('Você PERDEU!')
            print('{}'.format('-' * 40))
            break
    elif escolha == 'I':
        if result % 2 == 1:
            print('Você VENCEU!')
            print('{}'.format('-' * 40))
            cont += 1
        else:
            print('Você PERDEU!')
            print('{}'.format('-' * 40))
            break
    print('Vamos jogar novamente....')
    print('{}'.format('-'*40))
print(f'GAME OVER! Você ganhou {cont} vezes.')
