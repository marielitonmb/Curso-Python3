# Aula 23 - Desafio 114: Site esta acessivel?
# Criar um codigo em Python que teste se o site pudim.com.br esta acessivel pelo computador usado.
# Obs: soh precisa mostrar um print na tela se ta ou nao acessando o site.

from requests import get

try:
    url = get('http://pudim.com.br/')
except:
    print(f'O site \033[1;4m{"pudim.com.br"}\033[m não está acessível no momento.')
else:
    print(f'O site \033[1;4m{"pudim.com.br"}\033[m está acessível!')

# outra maneira
'''
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Nao foi possivel acessar o site Pudim.')
else:
    print('Foi possivel acessar o site Pudim!')
    #print(site.read())  # p/ pegar o conteudo do site
'''