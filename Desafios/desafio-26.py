# Aula 9 - Desafio 26: Primeira e ultima ocorrencia de uma string
# Ler uma frase e responder:
# quantas vezes aparece a letra A
# qual a posição que ela aparece na primeira vez
# qual a posição que ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip().lower()

cont = frase.count('a')
pos_i = frase.find('a')
pos_f = frase.rfind('a')

print(f'A letra "a" aparece na frase {cont} vezes.')
print(f'Ela aparece pela 1º vez na posiçao {pos_i} e por ultimo na posiçao {pos_f}.')
