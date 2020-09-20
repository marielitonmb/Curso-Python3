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
