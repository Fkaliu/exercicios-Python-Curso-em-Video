#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
totalidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    print('{} {} PESSOA {}'.format('-'*5, c, '-'*5))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totalidade += idade
    if c == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade> maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'F':
            mulher20 += 1
mediaidade = totalidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Tem {} mulheres com menos de 20 anos'.format(mulher20))
