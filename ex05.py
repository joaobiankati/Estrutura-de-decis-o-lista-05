trabalho = float(input('Informe a função que você trabalha, (1) Test, (2) ADT, (3) P, (4) ADS, (5) DBA,: '))
horas_t = float(input('Informe quantas horas você trabalha: '))

if trabalho == 1:
    valor_h = 20
elif trabalho == 2:
    valor_h = 35
elif trabalho == 3:
    valor_h = 45
elif trabalho == 4:
    valor_h = 40
elif trabalho == 5:
    valor_h = 50
else:
    print('Trabalho inválido!')
    valor_h = 0

salario = horas_t * valor_h

print(f'Seu salário é de {salario}')
