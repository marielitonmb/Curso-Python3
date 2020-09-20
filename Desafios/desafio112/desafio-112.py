# Aula 22 - Desafio 112: Entrada de dados monetarios
# Dentro do pacote utilidadesCeV que foi criado no desafio 111, temos um modulo chamado dado.
# Criar uma funçao chamada leiaDinheiro() que seja capaz de funcionar como a funçao input(),
# mas com uma validaçao de dados para aceitar apenas valores que sejam monetarios (digitos).

from desafio112.utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite o preço:')
moeda.resumo(p, 15, 8)
