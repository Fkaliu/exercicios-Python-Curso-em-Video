#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('{}'.format('-'*40))
    if tab <= 0:
        print('PROGRAMA ENCERRADO. Volte sempre')
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(tab, c, tab*c))
    print('{}'.format('-'*40))
