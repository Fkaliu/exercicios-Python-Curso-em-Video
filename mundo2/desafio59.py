#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar | [ 2 ] multiplicar | [ 3 ] maior | [ 4 ] novos números | [ 5 ] sair do programa // Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
fim = False
while not fim:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('{} Qual é a sua opção? '.format('>' * 7)))
    if opcao == 5:
        fim = True
    else:
        if opcao == 1:
            soma = n1 + n2
            print('A soma entre {} e {} é {}'.format(n1, n2, soma))
            print('{}'.format('='*30))
        elif opcao == 2:
            mult = n1 * n2
            print('O resultado entre {} x {} é {}'.format(n1, n2, mult))
            print('{}'.format('='*20))
        elif opcao == 3:
            maior = n1
            if n2 > maior:
                maior = n2
            print('O numero maior entre {} e {} é {}'.format(n1, n2, maior))
            print('{}'.format('='*30))
        elif opcao == 4:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        else:
            print('Opção invalida. Digite novamente.')
            print('{}'.format('='*30))
print('Fim do programa.')
