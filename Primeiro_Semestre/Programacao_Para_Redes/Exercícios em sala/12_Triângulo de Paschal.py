print("TRIÂNGULO DE PASCHAL\n")


try:
    N = int(input("Informe as N linhas do triângulo: "))

    CONT = 1
    L_PRINCIPAL = []
    L_AUXILIAR = []
    N_REVERSO = N - 1
    
    while CONT <= N:
        if len(L_PRINCIPAL) == 0:
            L_PRINCIPAL.append(CONT)
        else:
            if len(L_PRINCIPAL) == 1:
                L_PRINCIPAL.append(1)
            else:
                TEMP = L_PRINCIPAL[1]
                L_PRINCIPAL[1] = (L_PRINCIPAL[0] + L_PRINCIPAL[1])
                L_PRINCIPAL.append(TEMP)

        N_REVERSO -= 1
                
        
        for t in L_PRINCIPAL:
            print(f"{t}",end="")
        print("")

        CONT += 1
    
except Exception as e:
    print("[ERRO] - Número informado inválido:",e)
