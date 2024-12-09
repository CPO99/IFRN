print("Funções:")
print("- Informar quantidade de primos até X número")
print("- Somar primos até X número")
print("- Mostrar o primeiro primo cujo a soma dos dois primeiros dígitos é 10\n")

N = int(input("Informe até qual número verificar: "))

CONT_PRIMO = 0
SOMA_PRIMO = 0
SOMA_10 = 0

VER = 0
VER_2 = 1

while VER_2 <= N:
    CONT = 2
    
    while CONT < VER_2:
        if VER_2 % CONT == 0:
            VER += 1
        CONT += 1
        
    if VER == 0:
        print(VER_2)
        SOMA_PRIMO += VER_2
        CONT_PRIMO += 1
        
        VER_3 = VER_2
        
        primeiro_d = 0
        segundo_d = 0
        
        while VER_3 > 0:
            primeiro_d = segundo_d
            segundo_d = VER_3 % 10

            VER_3 = VER_3 // 10

        if primeiro_d + segundo_d == 10:
            SOMA_10 = VER_2

            
    VER = 0
    VER_2 += 1

print("\nSoma primos:",SOMA_PRIMO)
print("Quantidade de primos:",CONT_PRIMO)
print("Primo com dois primeiros dígitos soma 10:",SOMA_10)
        
