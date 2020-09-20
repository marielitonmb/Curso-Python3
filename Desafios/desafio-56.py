# Aula 13 - Desafio 56: Analisador completo
# Ler o nome, idade e sexo de 4 pessoas. No final devera mostrar:
# - media de idade do grupo
# - o nome do homem mais velho
# - quantas mulheres tem menos de 21 anos

nome = []
idade = []
sexo = []
media, mulheres, homem = 0, 0, 0
velho = ''

for i in range(0, 4):
    print('-'*5, f'{i+1}ª PESSOA', '-'*5)
    nome.append(input(f'\033[1;mNome:\033[m '))
    idade.append(int(input(f'\033[1;mIdade:\033[m ')))
    sexo.append(input(f'\033[1;mSexo [M/F]:\033[m ').lower())

media = sum(idade) / len(idade)

for i in range(0, 4):
    if sexo[i] == 'm' and idade[i] != 0:
        homem = max(idade)
        velho = nome[i]

    elif sexo[i] == 'f' and idade[i] < 21:
        mulheres += 1
print()
print(f'A media de idade do grupo eh de \033[1;4m{media:.1f} anos\033[m')
print(f'\033[1;4m{velho}\033[m eh o homem mais velho do grupo e ele tem \033[1;4m{homem} anos\033[m.')
print(f'No grupo, \033[1;4m{mulheres} mulher(es)\033[m tem menos de 21 anos.')

'''
### outro jeito ###

soma, media, idadehomem, jovens = 0, 0, 0, 0
nomehomem = ''

for p in range(1, 5):
    print(f'--- {p}ª PESSOA ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade

    if p == 1 and sexo in 'mM':
        idadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome
    if sexo in 'fF' and idade < 20:
        jovens += 1
media = soma / 4

print(f'A media de idade do grupo eh de {media:.2f} anos.')
print(f'{nomehomem} eh o mais velho do grupo e ele tem {idadehomem} anos.')
print(f'No grupo, {jovens} mulher(es) tem menos de 20 anos.')
'''