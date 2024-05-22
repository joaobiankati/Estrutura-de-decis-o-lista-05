def calcular_fatura(consumo):
    taxa_fixa = 34.49
    v_total = taxa_fixa

    if consumo > 30:
        v_total += (consumo - 30) * 10.19
        consumo = 30

    if consumo > 20:
        v_total += (consumo - 20) * 6.02
        consumo = 20

    if consumo > 15:
        v_total += (consumo - 15) * 5.97
        consumo = 15

    if consumo > 10:
        v_total += (consumo - 10) * 5.94
        consumo = 10

    if consumo > 5:
        v_total += (consumo - 5) * 1.07

    return v_total

consumo_m3 = float(input("Informe o consumo em m3: "))
v_fatura = calcular_fatura(consumo_m3)
print(f'O valor da sua fatura é: R$ {v_fatura:.2f}')