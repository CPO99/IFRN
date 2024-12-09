print("INVERTENDO NÚMEROS")

N = int(input("Informe um número com 3 dígitos: "))

CENTENA = N // 100
DEZENA = ((N - CENTENA * 100) // 10)
UNIDADE = (N - CENTENA * 100 - DEZENA * 10)

print("")

print(UNIDADE,DEZENA,CENTENA)

