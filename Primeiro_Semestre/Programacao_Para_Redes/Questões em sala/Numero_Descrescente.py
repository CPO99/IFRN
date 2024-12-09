print("VERIFICANDO NÚMERO DECRESCENTE\n")

try:
    N = int(input("Informe um número de 4 dígitos: "))

    U = N % 10
    N = N // 10
    
    D = N % 10
    N = N // 10
    
    C = N % 10
    N = N // 10

    UM = N

    if UM > C:
        if C > D:
            if D > U:
                print("\nO NÚMERO INFORMADO É DESCRESCENTE")
            else:
                print("\nNÚMERO NÃO DESCRESCENTE")
        else:
            print("\nNÚMERO NÃO DESCRESCENTE")
    else:
        print("\nNÚMERO NÃO DESCRESCENTE")

except:
    print("\nNÚMERO INVÁLIDO")


