# Aula 21 - Desafio 104: Validando entrada de dados em Python
# Criar uma funçao chamada leiaInt(), que vai funcionar de forma semelhante a funçao input().
# A diferença e que ela fara a validaçao para aceitar apenas um valor numerico.
# Ex: n = leiaInt('Digite um numero:')

def leiaInt(txt):
    while True:
        print(txt, end='')
        num = input()
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}.')

# outra maneira
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}.')
'''