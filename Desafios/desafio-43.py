# Aula 12 - Desafio 43: IMC Indice de Massa Corporal
# Leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status de acordo com a tabela:
# abaixo de 18.5 = Abaixo do peso
# entre 18.6 e 24.9 = Peso ideal
# de 25 ate 30 = Sobrepeso
# de 31 ate 39.9 = Obesidade
# acima de 40 = Obesidade morbida

peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura em m: '))
imc = peso / (altura ** 2)
print(f'\033[7mIMC = {imc:.1f}\033[m')

if imc <= 18.5:
    print('Voce esta \033[1mABAIXO DO PESO IDEAL!\033[m')
elif 18.6 <= imc <= 24.9:
    print('Voce esta no \033[1mPESO IDEAL!\033[m')
elif 25 <= imc <= 30.9:
    print('Voce esta com \033[1mSOBREPESO!\033[m')
elif 31 <= imc <= 39.9:
    print('Voce esta com \033[1mOBESIDADE!\033[m')
elif imc >= 40:
    print('Voce esta com \033[1mOBESIDADE MORBIDA!\033[m')
