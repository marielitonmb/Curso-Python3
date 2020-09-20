# Aula 9 - Desafio 23: Separando digitos de um numero
# Leia um numero entre 0 e 9999 e monstre na tela ele decomposto em:
# unidade, dezena, centena e milhar

num = input('Informe um numero de 0 a 9999: ')

if len(num) == 1:
    print(f'Unidade: {num[0]}')

elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')

elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')

elif len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')

else:
    print('Numero acima do esperado!')

print('\n# --- Metodo matematico --- #')
u = int(num) // 1 % 10
d = int(num) // 10 % 10
c = int(num) // 100 % 10
m = int(num) // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
