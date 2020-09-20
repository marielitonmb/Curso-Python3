# Aula 19 - Desafio 94: Unindo dicionarios e listas
# Ler o nome, sexo e idade de varias pessoas guardando os dados de cada pessoa num dicionario.
# Todos os dicionarios devem ficar numa lista.
# No final, mostrar:
# - quantas pessoas foram cadastradas
# - a media de idade do grupo
# - uma lista com todas as mulheres
# - uma lista com todas as pessoas com idade acima da media

dados = {}
lista = []
mulheres = []
acima = []
media = soma = 0

while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] not in 'FM':
            print('Informaçao invalida! Digite apenas M ou F.')
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']

    lista.append(dados.copy())

    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
        if opcao not in 'sn':
            print('Informaçao invalida! Digite apenas S ou N.')
    if opcao == 'n':
        break
    else:
        pass

media = soma / len(lista)
print('=+'*20)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'{media:.1f} anos eh a media de idade das pessoas cadastradas.')
print(f'Segue a lista das mulheres cadastradas:\n{mulheres}')
for item in lista:
    if item['idade'] >= media:
        acima.append(item['nome'])
print(f'Quem ficou com a idade acima da media foi:\n{[acima]}')
