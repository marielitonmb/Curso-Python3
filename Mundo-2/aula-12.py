# Aula 12 - Condições Aninhadas

nome = str(input('Qual o seu nome? ')).strip()

if nome == 'Marieliton' or nome == 'Leto':
    print('Que nome diferente!')
elif nome == 'Maria' or nome == 'Joao' or nome == 'Pedro':
    print('Seu nome eh bastante popular no Brasil.')
else:
    print('Seu nome eh bem comum.')

print(f'Ate mais, {nome}!')