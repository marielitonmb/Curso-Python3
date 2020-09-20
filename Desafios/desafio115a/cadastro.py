from time import sleep

def registro(nome, idade):
    arquivo = open('arquivo.txt', 'r')  # abrir o arquivo p/ leitura
    conteudo = arquivo.readlines()
    dado = nome + '   ' + str(idade) + ' anos' + '\n'
    conteudo.append(dado)  # insirir o conteúdo
    arquivo = open('arquivo.txt', 'w')  # Abre novamente o arquivo p/ escrita
    arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele
    arquivo.close()
    print(f'Registro de {nome} adicionado com sucesso.')
    sleep(2)
    return menu()

def mostrar():
    arquivo = open('arquivo.txt', 'r')
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    for linha in arquivo:
        print(f'{linha:<10}')
    arquivo.close()
    sleep(2)
    return menu()


def menu():
    while True:
        print('-' * 40)
        print('MENU PRINCIPAL'.center(40))
        print('-' * 40)
        print(f'\033[33m{"1"}\033[m \033[34m{"- Ver pessoas cadastradas"}\033[m')
        print(f'\033[33m{"2"}\033[m \033[34m{"- Cadastrar nova pessoa"}\033[m')
        print(f'\033[33m{"3"}\033[m \033[34m{"- Sair do sistema"}\033[m')
        print('-' * 40)
        try:
            resp = int(input(f'\033[32m{"Sua opçao >"}\033[m '))
        except (ValueError, TypeError):
            print('\033[31mOpçao invalida! Tente novamente.\033[m')
            sleep(1)
        else:
            if resp == 1:
                return mostrar()
            elif resp == 2:
                nome = str(input('Nome: ')).strip()
                idade = int(input('Idade: '))
                return registro(nome, idade)
            elif resp == 3:
                print('-' * 40)
                print('\033[7mSaindo do sitema...\033[m'.center(40))
                print('-' * 40)
                break
            else:
                print('\033[31mOpçao invalida! Tente novamente.\033[m')
                sleep(1)


