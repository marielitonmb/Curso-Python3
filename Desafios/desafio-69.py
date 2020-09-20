# Aula 15 - Desafio 69: Analise de dados do grupo
# Ler a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar
# se o usuario quer ou nao continuar. No final, mostrar:
# - quantas pessoas tem mais de 18 anos
# - quantos homens foram cadastrados
# - quantas mulheres tem menos de 20 anos
demaior = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        demaior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('*' * 20)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja contiuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'S':
        pass
    elif opcao == 'N':
        break
    print('*' * 20)

print(f'Ao todo, {demaior} pessoas tem mais de 18 anos.')
print(f'{homens} homem(ns) foi/foram cadastrado(s).')
print(f'{mulheres} mulher(es) tem menos de 20 anos')
