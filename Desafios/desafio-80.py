# Aula 17 - Desafio 80: Lista ordenada sem repetiçoes
# Ler 5 numeros e guarda-los numa lista, ja na posiçao correta de inserçao (s/ usar sort()).
# No final, mostrar a lista ordenada.

lista = list()

for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Numero adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Numero adicionado na posiçao {pos} da lista.')
                break
            pos += 1
print('=+'*25)
print(f'Os valores digitados em ordem, foram: {lista}')
