#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Em que cidade você nasceu? ')).strip()
cidade = cid.upper()
print('SANTO' in cidade)
print(cidade[:5] == 'SANTO')
