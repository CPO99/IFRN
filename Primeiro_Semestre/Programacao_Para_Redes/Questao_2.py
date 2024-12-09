print("CALCULANDO EQUAÇÃO DO SEGUNDO GRAU\n")

A = float(input("Informe o valor de A: "))
B = float(input("Informe o valor de B: "))
C = float(input("Informe o valor de C: "))

DELTA = (B**2-4*A*C)**(1/2)

X1 = (-B+DELTA)/(2*A)
X2 = (-B-DELTA)/(2*A)

print("\nValor X1: {}".format(X1))
print("Valor X2: {}".format(X2))

