# Aula 23 - Desafio 113: Funçoes aprofundadas em Python
# Reescrever a funçao leiaInt() do desafio 104, incluindo agora a possibilidade da digitaçao
# de um numero de tipo invalido.
# Criar tambem uma funçao leiaFloat() com a mesma funcionalidade.

def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            break
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            break
        else:
            return num


i = leiaInt('Digite um numero inteiro: ')
r = leiaFloat('Digite um numero real: ')

print(f'O valor inteiro digitado foi \033[1;4m{i}\033[m e o real foi \033[1;4m{r}\033[m!')
