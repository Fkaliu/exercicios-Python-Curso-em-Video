#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em BINÁRIO é: {}'.format(numero, bin(numero)[2:])) #[2:] serve para fatiar
elif opcao == 2:
    print('O número {} em OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em HEXADECIMAL é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou uma opção INVALIDA!')
#print(numero)
#print(opcao)
