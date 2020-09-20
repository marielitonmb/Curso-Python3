# Aula 20 - Desafio 97: Um print especial
# Criar uma funçao chamada escreva(), que receba um texto qualquer como parametro
# e mostre a mensagem com tamanho adaptavel.

def escreva(txt):
    tam = len(txt) + 2
    print('-' * tam)
    print(f' {txt}')
    print('-' * tam)

escreva('Teste')
escreva('Curso de Python')
escreva('Que a Força esteja com voce.')
escreva('Oxente!')
