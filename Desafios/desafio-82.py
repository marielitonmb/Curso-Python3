# Aula 17 - Desafio 82: Dividindo valores em varias listas
# Ler varios numeros e coloca-los numa lista. Depois disso, criar duas listas, onde:
# - uma guarda os valores par e a outra os valores impares
# No final, mostrar o conteudo das tres listas

lista = []
par = []
impar = []

while True:
    num = int(input('Informe um numero acima de 0: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

    continua = ' '
    while continua not in 'sn':
        continua = str(input('Deseja continuar [s/n]? ')).lower().strip()[0]
    if continua == 'n':
        break
    else:
        pass

print('='*30)
print('\033[7mLista completa:\033[m')
print(lista)
print('\033[7mLista com numeros PARES:\033[m')
print(par)
print('\033[7mLista com numeros IMPARES:\033[m')
print(impar)
