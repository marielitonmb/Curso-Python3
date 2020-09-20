# Aula 12 - Desafio 41: Classificando atletas
# Leia o ano de nascimento de um candidato a atleta de nataçao e de acordo com a idade informar:
# ate 9 anos: MIRIM
# ate 14 anos: INFANTIL
# ate 19 anos: JUNIOR
# ate 25 anos: SENIOR
# acima: MASTER

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('voce eh da categoria \033[1mMIRIM\033[m')
elif idade <= 14:
    print('Voce eh da categoria \033[1mINFANTIL\033[m')
elif idade <= 19:
    print('Vce eh da categoria \033[1mJUNIOR\033[m')
elif idade <= 25:
    print('Voce eh da categoria \033[1mSENIOR\033[m')
else:
    print('Voce eh da categoria \033[1mMASTER\033[m')
