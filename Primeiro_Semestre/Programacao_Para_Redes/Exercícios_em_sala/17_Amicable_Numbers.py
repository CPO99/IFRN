def divisoresSoma(n):
    soma = 0
    
    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma

print (divisoresSoma(10))
        
num_soma = []
    
for i in range(1, 10000):
    num_soma.append([i, divisoresSoma(i)])

num_soma.sort(key=lambda x: x[1])

for i in num_soma:
    print (i)
