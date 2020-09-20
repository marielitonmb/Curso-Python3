# Aula 10 - Condições (Parte 1)

'''
nome = str(input('Informe seu nome: ')).strip()

if nome == 'Marieliton':
    print('Que nome diferente!')
else:
    print('Seu nome e bem comum.')
print(f'Ola, {nome}')
'''

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))

m = (n1 + n2)/2

print(f'Sua media foi {m:.1f}')
print('Parabens!' if m >= 6 else 'Estude mais!')
