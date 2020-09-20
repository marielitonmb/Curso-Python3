# Aula 9 - Desafio 24: Verificando as primeiras letras de um texto
# Ler o nome de uma cidade e informar se começa com a palavra 'Santo' ou nao

cidade = str(input('Informe o nome de uma cidade: ')).strip().upper()

if 'SANTO' in cidade:
    print('A cidade \033[4;37mTEM\033[m "Santo" no nome')
else:
    print('A cidade \033[4;37mNAO TEM\033[m "Santo" no nome')
