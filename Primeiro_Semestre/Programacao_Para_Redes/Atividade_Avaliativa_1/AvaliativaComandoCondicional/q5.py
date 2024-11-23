print("INFORMANDO O DIA JULIANO\n")

try:
    ANO = int(input("Informe o ano: "))
    MES = int(input("Informe o mês: "))
    DIA = int(input("Informe o dia: "))
    
    BISSEXTO = 0 #bissexto como 1 ou 0 para somar aos dias na contagem no decorrer do codigo

    #verificando se ano é bissexto
    if ANO % 400 == 0:
        BISSEXTO = 1
    else:
        if ANO % 4 == 0 and ANO % 100 != 0:
            BISSEXTO = 1
    
    if MES == 1:
        if DIA >= 1 and DIA <= 31: #verificando o intervalo de dias do mes
            print("-\n- Dia Juliano",DIA)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 2: #fevereiro tem duas verificacoes de dias devido ao ano bissexto aumentar ou diminuir um dia desse mes
        if BISSEXTO == 1:
            if DIA >= 1 and DIA <= 29:
                print("\n- Dia juliano",31 + DIA)
            else:
                print("\n[ERRO] - Dia informado inválido!!!") 
        else:
            if DIA >= 1 and DIA <= 28:
                print("\n- Dia juliano",31 + DIA)
            else:
                print("\n[ERRO] - Dia informado inválido!!!") 
    elif MES == 3:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",59 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 4:
        if DIA >= 1 and DIA <= 30:
            print("\n- Dia juliano",90 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 5:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",120 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 6:
        if DIA >= 1 and DIA <= 30:
            print("\n- Dia juliano",151 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 7:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",181 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 8:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",212 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 9:
        if DIA >= 1 and DIA <= 30:
            print("\n- Dia juliano",243 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 10:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",273 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 11:
        if DIA >= 1 and DIA <= 30:
            print("\n- Dia juliano",304 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    elif MES == 12:
        if DIA >= 1 and DIA <= 31:
            print("\n- Dia juliano",334 + DIA + BISSEXTO)
        else:
            print("\n[ERRO] - Dia informado inválido!!!")
    else:
        print("\n[ERRO] - Mês informado inválido, informar entre 1 e 12, para janeiro a dezembro")
except:
    print("\n[ERRO] - Dados informados incorretamente. Informe dados válidos!")

    
