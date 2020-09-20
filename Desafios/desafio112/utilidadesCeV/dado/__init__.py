def leiaDinheiro(txt):
    while True:
        print(txt, end='')
        num = str(input()).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[31mERRO! \'{num}\' eh um preço invalido!\033[m')
        else:
            return float(num)
