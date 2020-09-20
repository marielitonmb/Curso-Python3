# Aula 18 - Listas (Parte 2)

teste = list()
teste.append('Marieliton')
teste.append(33)
galera = list()
#galera.append(teste)  # fazer isso cria uma dependencia entre as listas
galera.append(teste[:])  # isso faz a copia da lista sem criar dependencia
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste)
print(galera)
# ---------------------

galera = [['Joao', 19], ['Ana', 31], ['Manoel', 42], ['Maria', 51]]
#print(galera[3][0])
#print(galera[2][1])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
# ---------------------

galera = list()
dado = []
demaior = demenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} eh maior de idade.')
        demaior += 1
    else:
        print(f'{pessoa[0]} eh menor de idade.')
        demenor += 1

print(f'Temos {demaior} maiores e {demenor} menores de idade.')
