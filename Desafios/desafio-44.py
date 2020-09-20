# Aula 12 - Desafio 44: Gerenciador de pagamentos
# Calcular o valor de um produto considerando seu preço normal e condiçao de pagamento:
# a vista dinheiro/cheque = 10% de desconto
# a vista no cartao = 5% de desconto
# em ate 2x no cartao = preço normal
# 3x ou mais no cartao = 20% de juros
import time

preco = float(input('Informe o preço do produto R$: '))
print('#'*5, '\033[7mEscolha a forma de pagamento listada abaixo\033[m', '#'*5)
print('1 - pagamento a vista dinheiro/cheque (10% de desconto)\n'
      '2 - pagamento a vista no cartao (5% de desconto)\n'
      '3 - pagamento parcelado em 2x no cartao (s/ desconto)\n'
      '4 - pagamento parcelado em 3x ou mais no cartao (20% de juros)')
pag = int(input('Digite a opçao desejada: '))
print()

if pag == 1:
    print('Procesando a compra...')
    print()
    time.sleep(2)
    print('\033[1;46m*** Obrigado pela compra! ***\033[m')
    print(f'O valor final com 10% de desconto fica R${preco - (preco*0.1):.2f}')

elif pag == 2:
    print('Procesando a compra...')
    print()
    time.sleep(2)
    print('\033[1;46m*** Obrigado pela compra! ***\033[m')
    print(f'O valor final com 5% de desconto fica R${preco - (preco*0.05):.2f}')

elif pag == 3:
    print('Procesando a compra...')
    print()
    time.sleep(2)
    print('\033[1;46m*** Obrigado pela compra! ***\033[m')
    print(f'O valor final ficara parcelado em 2x de R${preco / 2:.2f}')

elif pag == 4:
    parcelas = int(input('Deseja parcelar em 3x? Se sim digite "0", caso contrario, digite quantas parcelas quer: '))

    if parcelas == 0:
        print('Procesando a compra...')
        time.sleep(2)
        print()
        print('\033[1;46m*** Obrigado pela compra! ***\033[m')
        print(f'O valor final ficara parcelado em 3x de R${(preco + (preco*0.2))/3:.2f}')

    elif parcelas <= 3:
        print('\033[7mOpçao invalida\033[m')

    elif parcelas > 3:
        print('Procesando compra...')
        time.sleep(2)
        print()
        print('\033[1;46m*** Obrigado pela compra! ***\033[m')
        print(f'O valor final ficara parcelado em {parcelas}x de R${(preco + (preco*0.2))/parcelas:.2f}')

else:
    print('\033[7mNao existe essa forma de pagamento\033[m')
