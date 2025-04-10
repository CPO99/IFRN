print("CALCULADORA DE SUB-REDE - IPV4\n")

def validaIp(ip):
    octetos = []
    try:
        if len(ip.split(".")) == 4:
            for n in ip.split("."):
                octetos.append(int(n))
            return True
        else:
            return False
    except:
        return False

def validaMasc(masc_ini, masc_fim):
    try:
        masc_ini = int(masc_ini)
        masc_fim = int(masc_fim)

        if masc_ini == masc_fim or masc_ini < masc_fim:
            return True
        else:
            return False
    except:
        return False
        
ip = input("Informe o endereço IP: ")

while validaIp(ip) == False:
    print("\n[ERRO] - Dados inválidos, tente novamente...\n")
    ip = input("Informe o endereço IP: ")

sub_rede_ini = input("\nInforme a máscara de sub rede inicial (CDIR): /")

sub_rede_fim = input("Informe a máscara de sub rede final (CDIR): /")

while validaMasc(sub_rede_ini, sub_rede_fim) == False:
    print("\n[ERRO] - Máscara de sub rede inválida...\n")
    sub_rede_ini = input("Informe a máscara de sub rede inicial (CDIR): /")
    sub_rede_fim = input("Informe a máscara de sub rede final (CDIR): /")

    if validaMasc(sub_rede_ini, sub_rede_fim) == True:
        sub_rede_ini = int(sub_rede_ini)
        sub_rede_fim = int(sub_rede_fim)




