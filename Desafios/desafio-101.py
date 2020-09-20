# Aula 21 - Desafio 101: Funçoes para votaçao
# Criar uma funçao chamada voto() que recebe como parametro o ano de nascimento de uma pessoa.
# A funçao deve retornar um valor literal indicando se uma pessoa tem voto:
# NEGADO (abaixo dos 16 anos), OPCIONAL (acima dos 65 anos e entre 16 e 18 anos) e OBRIGATORIO.
# Obs: dizer a idade da pessoa na tela.

def voto(n):
    from datetime import date

    idade = date.today().year - n
    if idade < 16:
        return f'Voce tem {idade} anos: NAO VOTA!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Voce tem {idade} anos: VOTO OPCIONAL'
    else:
        return f'Voce tem {idade} anos: VOTO OBRIGATORIO'


nasc = int(input('Informe o seu ano de nascimento: '))
print(voto(nasc))
