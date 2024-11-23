print("VERIFICANDO ANO BISSEXTO\n")

ANO = int(input("Informe o ano a ser verificado: "))

VER = ""

if ANO % 400 != 0:
    if ANO % 4 != 0 or ANO % 100 == 0:
        VER = "não "  

print("\n- O ano",ANO,VER + "é bissexto")
