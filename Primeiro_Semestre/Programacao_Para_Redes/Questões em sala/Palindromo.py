print("VERIFICANDO SE É PALÍNDROMO")

try: 
    N = int(input("\nInforme um número de 3 dígitos: "))

    if N < 0:
        N *= -1

    if N < 999 or N > 100:
        U = N % 10
        C = N // 100
        if U == C:
            print("\nO número é um palíndromo")
        else:
            print("\nO número não é um palíndromo")
    else:
        print("\n\nNÚMERO INVÁLIDO!!!")
except:
    print("\n\nNÚMERO INVÁLIDO!!!")
