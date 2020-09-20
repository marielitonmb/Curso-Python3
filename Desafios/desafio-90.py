# Aula 19 - Desafio 90: Dicionario em Python
# Ler o nome e a media de um aluno, guardando tambem a situaçao.
# No final, mostrar o conteudo da estrutura na tela.
# Quando for ler a media, ja incluir o nome do aluno.
'''
Nome eh igual a ----
Media eh igual a --
Situaçao eh igual a [Aprovado/Reprovado]
'''

aluno = {}

aluno['nome'] = str(input('Informe o nome do aluno: ')).strip().capitalize()
aluno['media'] = float(input(f'Informe a media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'

print('=+'*20)
for key, valor in aluno.items():
    print(f'{key} eh igual a {valor}')
