# Aula 14 - Desafio 57: Validaçao de dados
# Ler o sexo de uma pessoa, mas soh aceitar valores 'M' ou 'F'.
# Caso esteja errado a digitaçao, pedir pra digitar novamente ate ter o valor correto.

loop = True
while loop:
    sexo = input('Informe seu sexo [M/F]: ').lower().strip()[0]  # pega so o 1º caracter
    if sexo != 'm' and sexo != 'f':
        print('Voce digitou errado! Tente novamente.')
    else:
        print(f'Dado registrado! Sexo {sexo.upper()}.')
        loop = False

print('FIM DO LOOP!')
