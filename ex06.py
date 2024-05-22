def verificar_indice(indice_poluicao):
    if 0.05 <= indice_poluicao <= 0.25:
        print('O índice de poluição esta aceitavel. Nenhuma ação necessária!')
    elif 0.25 < indice_poluicao <= 0.30:
        print('Industrias de 1 grau devem suspender as atividades!')
    elif 0.31 <= indice_poluicao <= 0.40:
        print('Industrias de 1 e 2 grau devem suspender as atividades!')
    elif indice_poluicao > 0.41:
        print('Todos grupos precisaram suspender as ativdades!')

indice_poluicao = float(input("Informe o indice de poluição: "))
verificar_indice(indice_poluicao)