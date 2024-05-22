custo_internet = 0.50 #Mb
custo_local = 0.35 #min
custo_interurbana = 0.60 #min
custo_torpedo = 0.20 #torpedo

consumo_internet = float(input("Informe o consumo da internet em Mb: "))
total = custo_internet * consumo_internet

consumo_local = float(input("Informe o consumo da internet local por minutos: "))
total2 = custo_local * consumo_local

consumo_interurbana = float(input("Informe o consumo interurbana em minutos: "))
total3 = custo_interurbana * consumo_interurbana


consumo_torpedo = float(input("Informe o consumo do torpedo: "))
total4 = custo_torpedo * consumo_torpedo

total_fatura_sem_desconto = total + total2 + total3 + total4

desconto_internet = 0
desconto_local = 0
desconto_interurbana = 0
desconto_torpedo = 0

if consumo_internet > 50:
    desconto_internet = consumo_internet * 0.05
elif consumo_local > 200:
    desconto_local = consumo_local * 0.10
elif consumo_interurbana > 150:
    desconto_interurbana = consumo_interurbana * 0.10
elif consumo_torpedo > 50:
    desconto_torpedo = consumo_torpedo * 0.20

maior_desconto = max(desconto_internet, desconto_local, desconto_interurbana, desconto_torpedo)

if maior_desconto == desconto_internet:
    tipo_desconto = "Internet"
    valor_desconto = desconto_internet

elif maior_desconto == desconto_local:
    tipo_desconto = "Local"
    valor_desconto = desconto_local

elif maior_desconto == desconto_interurbana:
    tipo_desconto = "Interurbana"
    valor_desconto = desconto_interurbana

else:
    tipo_desconto = "Torpedo"
    valor_desconto = desconto_torpedo

valor_total_com_desconto = total_fatura_sem_desconto - valor_desconto

print(f'O valor total da fatura é de R$ {total_fatura_sem_desconto}')
print(f'O tipo de desconto feito foi {tipo_desconto}')
print(f'O valor do desconto é de R$ {valor_desconto}')
print(f'O valor total da fatura com o desconto é de R$ {valor_total_com_desconto}')