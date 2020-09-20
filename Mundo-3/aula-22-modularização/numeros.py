from uteis import numeros

num = int(input('Digite um numero: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} eh {fat}')
print(f'O dobro de {num} eh {numeros.dobro(num)}')
print(f'O triplo de {num} eh {numeros.triplo(num)}')
