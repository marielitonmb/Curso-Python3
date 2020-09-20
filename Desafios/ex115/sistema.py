from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar um novo dado no arquivo
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Informe uma opçao valida!\033[m')
    sleep(2)
