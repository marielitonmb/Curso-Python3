# Aula 17 - Desafio 83: Validando expressoes matematicas
# Ler uma expressao qualquer que use parenteses. O programa devera analisar se a expressao
# passada esta com os parenteses abertos e fechados na ordem correta.
# Ex: ((a+b)*c)), isso ta errado

equacoes = []
abreP = fechaP = 0

equacoes.append(input('Informe a expressao matematica: ').strip())
for valores in equacoes:
    for caracter in valores:
        if caracter == '(':
            abreP += 1
        elif caracter == ')':
            fechaP += 1

if abreP == fechaP:
    print('A expressao esta correta!')
elif abreP > fechaP:
    print('Voce esqueceu de FECHAR algum parenteses!')
elif abreP < fechaP:
    print('Voce esqueceu de ABRIR algum parenteses!')

# outra maneira
'''
expr = str(input('Digite a expressao: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressao valida!')
else:
    print('Expressao invalida!')
'''