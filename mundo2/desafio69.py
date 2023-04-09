#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
homens = mulher20 = mais18 = 0
print('CADASTRE UMA PESSOA')
print('{}'.format('-'*40))
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('{}'.format('-'*40))
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    escolha = ' '
    while escolha not in 'SN':
       escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('{}'.format('-' * 40))
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {mais18}')
print(f'Ao todo temos {homens} cadastrados.')
print(f'E temos {mulher20} com menos de 20 anos.')
