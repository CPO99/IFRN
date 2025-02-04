print("SEQUÊNCIA DE COLATZ\n")

try:
    N = int(input("Informe um número inteiro: "))
    print(N)
    while N > 1:
        if N % 2 == 0:
            N /= 2
        else:
            N = 3 * N + 1
        print(int(N))
except:
    print("\n[ERRO] - Número informado inválido")
