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
        masc_ini = masc_ini
        masc_fim = masc_fim

        if masc_ini == masc_fim or masc_ini < masc_fim:
            return True
        else:
            return False
    except:
        return False

def enderecoRede(sub_rede, ip):
    bits_rede = (32 - sub_rede) // 8

    octetos_binario_ip = []

    for i in ip.split("."):
        q = 9
        conv_bin = []
        
        div = int(i)
        while q != 0 or q != 1:
            conv_bin.append(div % 2)

            if div // 2 >= 1:
                div = div // 2

        print (conv_bin.reverse())
            
    """
    cont = 0
    
    for i in ip.split("."):
        if cont == 0:
            print(i,end="")
        elif cont < 4 - octetos:
            print(".%s",end="") % (i)
        else:
            print(".0",end="")

        cont += 1
    """
    
def primeiroUltimoHost(ip):
    pass
        
ip = input("Informe o endereço IP: ")

#laço para validar o endereço de IP
while validaIp(ip) == False:
    print("\n[ERRO] - Dados inválidos, tente novamente...\n")
    ip = input("Informe o endereço IP: ")

sub_rede_ini = int(input("\nInforme a máscara de sub rede inicial (CDIR): /"))

sub_rede_fim = int(input("Informe a máscara de sub rede final (CDIR): /"))

#laço para validar as máscaras de subrede
"""
while validaMasc(sub_rede_ini, sub_rede_fim) == False:
    print("\n[ERRO] - Máscara de sub rede inválida...\n")
    sub_rede_ini = input("Informe a máscara de sub rede inicial (CDIR): /")
    sub_rede_fim = input("Informe a máscara de sub rede final (CDIR): /")

    if validaMasc(sub_rede_ini, sub_rede_fim) == True:
        sub_rede_ini = int(sub_rede_ini)
        sub_rede_fim = int(sub_rede_fim)
"""

enderecoRede(sub_rede_ini, ip)




