# Aula 19 - Dicionários

pessoas = {'nome': 'Marieliton', 'sexo': 'M', 'idade': 33}  # ou pessoas = dict()
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-'*10)

for k in pessoas.keys():
    print(k)
print('-'*10)

pessoas['nome'] = 'Pedro'  # p/ modificar itens no dicionario
for v in pessoas.values():
    print(v)
print('-'*10)

del pessoas['sexo']  # deleta a key e seu conteudo do dicionario
pessoas['peso'] = 75.6  # p/ adicionar itens no dicionario
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*10)

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'Sao Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['UF'])
print(brasil[1]['Sigla'])
print('-'*10)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())  # p/ incluir itens de um dicionario numa lista use o .copy()
print('-'*10)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print('-'*10)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
