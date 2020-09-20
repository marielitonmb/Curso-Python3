# Aula 10 - Desafio 30: Par ou impar?

num = int(input('Digite um numero: '))

print('\033[7;40mEh PAR\033[m' if (num % 2) == 0 else '\033[7;40mEh IMPAR\033[m')
