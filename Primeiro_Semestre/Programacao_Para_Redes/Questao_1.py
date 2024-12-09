print ("CALCULANDO CÉDULAS PARA TROCO\n")

VALOR_TOTAL = float(input("Informe o valor da conta: "))
PAGAMENTO = float(input("Informe o valor do pagamento: "))

TROCO = PAGAMENTO - VALOR_TOTAL
print ("\nTroco: {}\n".format(TROCO))

print ("Cédulas de R$ 200:", TROCO // 200)
TROCO -= TROCO // 200 * 200

print ("Cédulas de R$ 100:", TROCO // 100)
TROCO -= TROCO // 100 * 100

print ("Cédulas de R$ 50:", TROCO // 50)
TROCO -= TROCO // 50 * 50

print ("Cédulas de R$ 20:", TROCO // 20)
TROCO -= TROCO // 20 * 20

print ("Cédulas de R$ 10:", TROCO // 10)
TROCO -= TROCO // 10 * 10

print ("Cédulas de R$ 5:", TROCO // 5)
TROCO -= TROCO // 5 * 5

print ("Cédulas de R$ 2:", TROCO // 2)
TROCO -= TROCO // 2 * 2

print ("Cédulas de R$ 1:", TROCO)
 

