# Aula 19 - Desafio 92: Cadastro de trabalhador em Python
# Ler o nome, ano de nascimento e carteira de trabalho e cadastrar (c/ idade, nao o ano de nasc) em um dicionario.
# Se a CTPS for diferente de zero, o dicionario recebe tambem o ano de contrataçao e o salario.
# Calcular e acrescentar, alem da idade, com quantos anos a pessoa vai se aposentar.
# Obs: se aposenta c/ 35 anos de carteira assinada

from datetime import datetime

cadastro = {}

cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.today().year - nasc
cadastro['ctps'] = int(input('CTPS [0 se nao tem]: '))
if cadastro['ctps'] != 0:
    cadastro['contrataçao'] = int(input('Ano de contrataçao: '))
    cadastro['salario'] = int(input('Salario R$: '))
    cadastro['aposentadoria'] = cadastro['contrataçao'] + 35
else:
    cadastro['aposentadoria'] = 0

print('=+'*20)
print(f'Voce se chama {cadastro["nome"]}.')
print(f'Tem {cadastro["idade"]} anos de idade.')
print(f'Possui a CTPS de nº {cadastro["ctps"]}.')
if cadastro['aposentadoria'] != 0:
    print(f'Ira se aposentar em {cadastro["aposentadoria"]} com'
          f' {cadastro["idade"] + (cadastro["aposentadoria"] - datetime.now().year)} anos.')
else:
    print(f'E no momento nao tem carteira assinada.')
