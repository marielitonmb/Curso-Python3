# Aula 7 - Desafio 8: Conversor de medidas

m = int(input('Informe a quatidade em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'{m}m equivale a: {km}km | {hm}hm | {dam}dam | {dm}dm | {cm}cm | {mm}mm')
