# Aula 9 - Desafio 22: Analisador de textos
# Ler o nome completo de uma pessoa e mostrar:
# o nome com todas as letras minusculas e tambem maiusculas
# o nome sem espaços
# quantas letras tem apenas o primeiro nome

nome = str(input('Digite um nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
div_nome = nome.split()
juntado = ''.join(div_nome)
print(f'Seu nome completo tem {len(juntado)} letras')
print(f'Seu primeiro nome tem {len(div_nome[0])} letras')
