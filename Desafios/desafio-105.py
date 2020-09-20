# Aula 21 - Desafio 105: Analisando e gerando dicionarios
# Criar uma funçao chamada notas() que pode receber varias notas de alunos e
# vai retornar um dicionario com as seguintes informaçoes:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a media da turma
# - a situaçao (opcional) (RUIM, RAZOAVEL, BOA, OTIMA dependendo da media)
# Obs: adicionar docstring p/ funçao.

def notas(*n, sit=False):
    """
    -> Dicionario que analisa e armazena as notas de um aluno.
    :param n: notas do aluno.
    :param sit: (Opcional) informa a situaçao do aluno de acordo com a sua media.
    :return: informa os dados contidos no dicionario.
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] < 5:
            dados['situaçao'] = 'RUIM'
        elif 5 <= dados['media'] < 7:
            dados['situaçao'] = 'RAZOAVEL'
        elif 7 <= dados['media'] < 8:
            dados['situaçao'] = 'BOA'
        elif dados['media'] >= 8:
            dados['situaçao'] = 'OTIMA'
    return dados


resp = notas(5.5, 7.5, 2.5, 9, sit=True)
print(resp)
help(notas)
