print("CALCULANDO MÉDIA ARITMÉTICA DE SÉRIE DE NÚMEROS")
print("- Informe um número negativo para parar\n")

NUMERO = 0
SOMA = 0
CONT = -1 #contador iniciando negativo para compensar a contagem do número negativo de parada

while NUMERO >= 0:
    SOMA += NUMERO
    CONT += 1
    
    NUMERO = int(input("Informe um número: "))

    

print("\nQuantidade de números informados:",CONT)
print("Média dos número informados:",SOMA / CONT if SOMA != 0 else "sem dados")
