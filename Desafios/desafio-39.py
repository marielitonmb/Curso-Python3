# Aula 12 - Desafio 39: Alistamento militar
# Leia o ano de nascimento do usuario e de acordo com a idade faça:
# se ele ainda vai se alistar ao serviço militar
# se eh a hora de se alistar (18 anos)
# se ja passou do tempo de alistamento
# o prog deve mostrar o tempo que falta ou o que passou do prazo

from datetime import date

sexo = str(input('Qual seu sexo, masculino [M] ou feminino [F]? ')).lower().strip()

if sexo == 'f':
    print('Voce do sexo feminio esta dispensada do alistamento militar.')

elif sexo == 'm':
    nasc = int(input('Informe seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc

    if idade < 18:
        print(f'Voce ainda eh jovem pra se alistar. Tem apenas {idade} anos.')
        print(f'Faltam {18 - idade } ano(s) pra voce se alistar no serviço militar.')
        print(f'{ano + (18 - idade)} sera o ano de seu alistamento.')

    elif idade == 18:
        print(f'Voce tem 18 anos, ja se alistou no serviço militar? Se nao, deveria.')

    elif idade > 18:
        print(f'Voce tem {idade} anos e nao se alistou no serviço militar?')
        print(f'Ja passou {idade - 18} ano(s) do prazo.')
        print(f'Deveria ter se alistado em {ano - (idade - 18)}.')

else:
    print('Opçao Invalida!')
