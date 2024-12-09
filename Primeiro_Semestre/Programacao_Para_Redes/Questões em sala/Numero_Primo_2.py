print("VERIFICANDO NÚMERO PRIMO\n")

N = int(input("Informe até quando parar: "))

CONT = 1
CONT_2 = 1
VER = 0

while CONT_2 <= N:
    while CONT < CONT_2:
        if CONT_2 % CONT == 0:
            VER += 1
        CONT += 1
    if VER == 1:
        print("\n- O número",CONT_2,"é primo")      
    VER = 0
    CONT = 1
    CONT_2 += 1
        
