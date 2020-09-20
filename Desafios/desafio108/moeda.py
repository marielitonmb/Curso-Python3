def aumentar(preço=0, taxa=0):
    return preço + ((preço * taxa) / 100)


def diminuir(preço=0, taxa=0):
    return preço - ((preço * taxa) / 100)


def dobro(preço=0):
    return preço * 2


def metade(preço=0):
    return preço / 2


def moeda(preço=0):
    return f'R${preço:.2f}'.replace('.', ',')
