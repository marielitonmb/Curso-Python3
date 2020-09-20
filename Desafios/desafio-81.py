# Aula 17 - Desafio 81: Extraindo dados de uma lista
# Ler varios numeros e coloca-los numa lista. Depois mostrar:
# - quantos numeros foram digitados
# - a lista ordenada de forma decrescente
# - se o valor 5 foi digitado e esta ou nao na lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continua == 'N':
        break
    elif continua == 'S':
        pass

print('='*30)
print(f'Foram digitados \033[1m{len(lista)}\033[m numeros na lista.')
print('Os valores informados foram:')
print(lista)
print('A lista em forma decrescente fica:')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 \033[4mfoi digitado\033[m.')
else:
    print('O valor 5 \033[4mnao foi digitado\033[m.')
