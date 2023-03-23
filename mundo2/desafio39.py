#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoatual = date.today().year
print('Escolha uma das opções abaixo:')
print('[ 1 ] Masculino')
print('[ 2 ] Feminino')
print('[ 3 ] Prefiro não informar')
opcao = int(input('Sua opção: '))
if opcao == 1:
    anonasc = int(input('Digite o ano do seu nascimento: '))
    idadeatual = anoatual - anonasc
    anoalista = anonasc + 18
    tempofalta = anoalista - anoatual
    print('Quem nasceu em {} tem {} anos em {}'.format(anonasc, idadeatual, anoatual))
    if anoalista == anoatual:
        print('Ta na sua hora filhão, vai se alistar')
    elif anoalista > anoatual:
        print('vc ainda tem tempo, aproveite.')
        print('ainda falta {} anos para o seu alistamento'.format(tempofalta))
        print('O seu ailstamento será em {}'.format(tempofalta + anoatual))
    else:
        print('ja passou a hora do seu alistamento.')
        print('vc se alistou em {}'.format(anoalista))
elif opcao == 2:
    print('Deu sorte')
elif opcao == 3:
    print('Para saber se vc deve se alistar vc deve informar o sexo')
else:
    print('Me ajuda a te ajudar')
#print('Nasceu em: {}'.format(anonasc))
#print('Se alista em: {}'.format(anoalista))
#print('idade atual {}'.format(idadeatual))
#print(tempofalta)
