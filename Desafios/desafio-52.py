# Aula 13 - Desafio 52: Numeros primos
# Ler um numero inteiro e dizer se ele eh ou nao primo

num = int(input('Digite um numero: '))

primo = 0
for n in range(1, num+1):
    if num % n == 0:
        primo += 1
        print('\033[1;32m', end=' ')
    else:
        print('\033[m', end=' ')
    print(f'{n}\033[m ', end='')
print()
if primo == 2:
    print(f'\nLogo \033[1m{num}\033[m \033[4mEH NUMERO PRIMO\033[m pois soh eh divisivel por {primo} numeros')
else:
    print(f'Logo \033[1m{num}\033[m \033[4mNAO EH NUMERO PRIMO\033[m pois eh divisiel por {primo} numeros')
