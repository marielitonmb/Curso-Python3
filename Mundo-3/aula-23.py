# Aula 23 - Tratamento de Erros e Exceções

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema...')  # evita que o programa encerre por conta de alguma exceçao
    print(f'Problema encontrado: {erro.__class__}')
else:
    print(f'O resultado eh {r:.1f}')
finally:
    print('Volte sempre!')  # sempre eh mostrado

#-----------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Nao eh possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else:
    print(f'O resultado eh {r:.1f}')
finally:
    print('Volte sempre!')  # sempre eh mostrado
