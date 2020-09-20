# Aula 9 - Desafio 25: Procurando uma string dentro de outra
# Leia um nome por completo e informe se consta a palavra 'Silva' nele

nome = str(input('Digite seu nome completo: ')).strip().lower()

if 'silva' in nome:
    print('Seu nome \033[1;36mTEM\033[m "Silva"')
else:
    print('Seu nome \033[1;36mNAO TEM\033[m "Silva"')
