print("VERIFICANDO NÚMERO PRIMO\n")

N = int(input("Informe um número (zero para parar): "))

CONT = 1
VER = 0

while N != 0:
    while CONT < N:
        if N % CONT == 0:
            VER += 1
        CONT += 1
    if VER > 1:
        print("\n- O número não é primo")
    else:
        print("\n- O número é primo")
    VER = 0
    CONT = 1
    N = int(input("\nInforme um número (zero para parar): "))
        
