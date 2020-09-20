# Aula 9 - Desafio 27: Primeiro e ultimo nome de uma pessoa
# Ler o nome completo de uma pessoa e responder com o primeiro e o ultimo nome

nome = str(input('Informe seu nome completo: ')).strip()

div_nome = nome.split()

print(f'Primeiro nome = {div_nome[0]}')
print(f'Ultimo nome = {div_nome[-1]}')  # {div_nome[len(div_nome)-1]}
