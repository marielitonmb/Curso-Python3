# Aula 12 - Desafio 36: Aprovando emprestimo
# - leia o valor da casa, o salario do comprador e quantos anos ira pagar a divida
# - calcular o valor da prestaçao mensal sem que exceda 30% do salario
# - se exceder os 30% o emprestimo sera negado

print('\033[1:7mPEDIDO DE EMPRESTIMO\033[m')
casa = float(input('Informe o valor da casa que deseja adquirir R$: '))
salario = float(input('Informe o seu salario R$: '))
tempo = int(input('Informe em quanto tempo (anos) pretende pagar o emprestimo: '))

limite = salario * 0.3
parcela = casa / (tempo * 12)

if parcela > limite:
    print('Emprestimo \033[1:41mNEGADO!\033[m')
    print('Voce nao possui renda o suficiente para pagar o emprestimo')
else:
    print('Parabens, emprestimo \033[1;32mAPROVADO!\033[m')
    print(f'A parcela de finaciamento ficara por \033[1;37mR${parcela:.2f}\033[m')
