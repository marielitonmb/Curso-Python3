# Aula 22 - Desafio 108: Formatando moedas em Python
# Adaptar o codigo do desafio 107 criando uma funçao adicional chamada moeda()
# que consiga mostrar os valores como um valor monetario formatado.
#Obs: eh pra colocar R$ e duas casas decimais nos prints.

from desafio108 import moeda

p = float(input('Digite um preço R$:'))

print(f'A metade de {moeda.moeda(p)} eh {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} eh {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
