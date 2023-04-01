#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('{} Os Termos de uma PA {}'.format('>'*10, '<'*10))
n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = n
c = 1
total = 0
novotermo = 10
while novotermo != 0:
    total = total+novotermo
    while c <= total:
        print('{} '.format(termo), end='')
        termo += razao
        c += 1
    print('pausa')
    novotermo = int(input('Quantos termos vc quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

