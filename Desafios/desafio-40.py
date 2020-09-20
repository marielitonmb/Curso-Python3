# Aula 12 - Desafio 40: Aquele classico da media
# Leia duas notas de um aluno e calcule a sua media mostrando uma mensagem de acordo com a media atingida:
# media abaixo de 5.0 = REPROVADO
# media entre 5.0 e 6.9 = RECUPERAÇAO
# media igual ou acima de 7.0 = APROVADO

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'\033[1;4;31mREPROVADO!\033[m Media = {media:.1f}')
elif 5 <= media < 7:
    print(f'\033[1;4;33mRECUPERAÇAO!\033[m Media = {media:.1f}')
elif media >= 7:
    print(f'\033[1;4;32mAPROVADO!\033[m Media = {media:.1f}')
