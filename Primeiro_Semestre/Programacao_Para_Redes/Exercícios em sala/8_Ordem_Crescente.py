print("NUMEROS EM ORDEM CRESCENTE\n")

LISTA = []

try:

    LISTA.append(int(input("Informe o primeiro número: ")))
    LISTA.append(int(input("Informe o segundo número: ")))
    LISTA.append(int(input("Informe o terceiro número: ")))

    print("")

    for i in range(len(LISTA)):
        for j in range(len(LISTA) - 1):
            if LISTA[j] > LISTA[j + 1]:
                INTER = LISTA[j]
                LISTA[j] = LISTA[j + 1]
                LISTA[j + 1] = INTER
    cont = 0               
    for i in LISTA:
        cont += 1
        print ("Numero {}: {}".format(cont, i))

except ValueError as err:
    print("\n\n[ERRO] - CONVERSÃO INADEQUADA")

