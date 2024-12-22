print("CALCULANDO MÉDIA ARITMÉTICA DE SÉRIE DE NÚMEROS")
print("- Informe um número negativo para parar\n")

NUMERO = 0
SOMA = 0
CONT = -1 #contador iniciando negativo para compensar a contagem do número negativo de parada

NUMEROS = []

while NUMERO >= 0:
    SOMA += NUMERO
    CONT += 1
    
    NUMERO = int(input("Informe um número: "))

    if NUMERO >= 0:
        NUMEROS.append(NUMERO)

SOMA_DP = 0

print (NUMEROS)

for num in NUMEROS:
    print ((num - (SOMA / CONT))**2)
    SOMA_DP += (num - (SOMA / CONT))**2
    
print("\nQuantidade de números informados:",CONT)
print("Média dos número informados:",SOMA / CONT if SOMA != 0 else "sem dados")
print("Desvio padrão:",(SOMA_DP /(CONT - 1)) ** (1/2))
