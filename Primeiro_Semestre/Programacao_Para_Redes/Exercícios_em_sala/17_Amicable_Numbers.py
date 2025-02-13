from functools import reduce

def divisoresSoma(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma
        
num_soma = []
    
for i in range(1, 10000):
    if divisoresSoma(divisoresSoma(i)) == i:
        if i + divisoresSoma(i) not in num_soma and divisoresSoma(i) != i:
            num_soma.append(i + divisoresSoma(i))
            
print(num_soma)
print(reduce(lambda x, y: x + y, num_soma))
print(num_soma)
