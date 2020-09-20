# Aula 9 - Manipulando Texto

frase = '  Curso em Video Python'
print(len(frase))  # Tamanho da string
print('Curso' in frase)  # Checa se um caracter estah numa string
print(frase.upper())  # Deixa tudo em caixa alta
print(frase.lower())  # Deixa tudo em caixa baixa
print(frase.replace('Python', 'Android'))  # Troca caracteres
print(frase.capitalize())  # Deixa soh o 1º caracter em maiusculo
print(frase.title())  # Deixa todos os 1º caracteres em maiusculo
print(frase.strip())  # Tira os espaços do inicio e fim da string (lstrip() e rstrip() tiram da esq e dir)
print(frase.split())  # Separa os caracteres em varias strings formando itens de uma lista
dividido = frase.split()
print(dividido[0:2])
print('-'.join(frase))  # Adiciona algo na string

#  Printar textos longos
print('''Ergamos um brinde aos amigos ausentes,
amores perdidos, velhos deuses e à Estação das Brumas,
e que cada um de nós sempre conceda ao diabo o que lhe é merecido.''')
