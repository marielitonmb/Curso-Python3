# Aula 13 - Desafio 51: Progressao aritmetica
# Leia o primeiro termo e a razao de uma PA. No final, mostrar os 10 primeiros termos dessa progressao
# a[n] = a[1] + (n - 1) * r

primeiro = int(input('Informe o primeiro valor da PA: '))
razao = int(input('Informe a razao da PA: '))
decimo = primeiro + (10 - 1) * razao

print('PA = ', end='')
for c in range(primeiro, decimo + razao, razao):
    print(f'{c} ->', end=' ')
print('FIM!')
