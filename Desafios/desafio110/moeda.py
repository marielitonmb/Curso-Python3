def aumentar(preço=0, taxa=0, aux=False):
    resp = preço + ((preço * taxa) / 100)
    return resp if aux is False else moeda(resp)


def diminuir(preço=0, taxa=0, aux=False):
    resp = preço - ((preço * taxa) / 100)
    return resp if aux is False else moeda(resp)


def dobro(preço=0, aux=False):
    resp = preço * 2
    return resp if not aux else moeda(resp)


def metade(preço=0, aux=False):
    resp = preço / 2
    return resp if not aux else moeda(resp)


def moeda(preço=0):
    return f'R${preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa1=0, taxa2=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print('Preço analizado:', f'\t{moeda(preço)}')
    print('Dobro do preço:', f'\t{dobro(preço, True)}')
    print('Metade do preço:', f'\t{metade(preço, True)}')
    print(f'{taxa1}% de aumento:', f'\t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de reduçao:', f'\t{diminuir(preço, taxa2, True)}')
    print('-' * 30)
