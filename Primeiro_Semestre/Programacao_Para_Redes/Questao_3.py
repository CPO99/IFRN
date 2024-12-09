print ("QUESTÃO 3 - CALCULANDO O MONTANTE\n")

CAPITAL = float(input("Informe o valor do capital: R$ "))
JUROS = float(input("Informe o valor dos juros (%): "))
TEMPO = float(input("Informe o tempo (meses): "))

M = CAPITAL * (1 + JUROS / 100)**TEMPO

print("\nValor do montante: R$ {:.2f}".format(M))