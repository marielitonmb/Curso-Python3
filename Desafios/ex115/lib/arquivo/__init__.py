from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # p/ ler arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # o sinal de '+' eh que permite a criaçao do arquivo
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('Pessoas cadastradas')
        #print(a.read())  # mostra o conteudo do arquivo s/ formataçao
        for linha in a:
            dado = linha.split(';')  # separa os dados entre o ';' e coloca numa lista
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')  # o 'a' eh de append, ele acrescenta algo novo no arquivo
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
