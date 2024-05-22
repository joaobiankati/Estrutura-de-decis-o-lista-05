num = int(input("Informe um número: "))
num2 = int(input("Informe um segundo número: "))
num3 = int(input("Informe um terceiro número: "))
if num > num2 and num > 3:
    print(f'O maior número é {num}')
elif num2 > num and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')