lado = float(input('Informe o lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))
if lado == lado2 == lado3:
    print('O triângulo é equilátero!')
elif lado != lado2 and lado2 != lado3 and lado3 != lado:
    print('O triângulo é escaleno!')
else:
    print('O triângulo é isósceles!')