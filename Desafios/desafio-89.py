# Aula 18 - Desafio 89: Boletim com listas compostas
# Ler o nome e duas notas de varios alunos e guardar tudo numa lista composta.
# No final, mostrar o boletim com a media de cada aluno e permitir que o usuario possa
# mostrar as notas de cada aluno individualmente.
'''
No  NOME  MEDIA
---------------
0   ---   0.0
1   ---   0.0
3   ---   0.0
---------------
Pergunta pelo indice do aluno e coloca um flag pra encerrar a solicitaçao
'''

boletim = list()
dados = list()
media = 0

while True:
    while len(dados) < 3:
        dados.append(str(input('Nome: ')).strip().upper())
        dados.append(float(input('1ª nota: ')))
        dados.append(float(input('2ª nota: ')))
    boletim.append(dados[:])
    dados.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        break
    else:
        pass

print('=+'*12)
print(f'{"No":<5} {"NOME":<8} {"MEDIA":>7}')
print('=+'*12)
for indice, item in enumerate(boletim):
    media = (item[1] + item[2]) / 2
    print(f'{indice:<5} {item[0]:<8} {media:>5.1f}')
print('=+'*12)

while True:
    print('-'*30)
    num = int(input('Digite o No do aluno p/ ver suas notas [999 p/ sair]: '))
    if num == 999:
        print('FIM!')
        break
    elif num > len(boletim):
        print('Aluno nao registrado!')
    else:
        print(f'As notas de {boletim[num][0]} foram {boletim[num][1]} e {boletim[num][2]}')

# outra maneira
'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break

print('=+'*30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":<8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno [999 interrompe]? '))
    if opc == 999:
        print('FIM!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
'''