# Aula 07 - Desafio 13: Reajuste salarial
# Ler o salario de um funcionario e calcular um aumento de 15%

salario = float(input('Informe seu salario: '))

print(f'Parabens, voce recebeu um abono de 15% no salario. Seu salario agora eh R${salario + (salario*0.15):.2f}')
