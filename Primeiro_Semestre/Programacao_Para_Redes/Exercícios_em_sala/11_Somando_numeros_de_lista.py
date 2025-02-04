L =  [1,2,3,4,5,6,7,8]

L2 = []

for i in range(0,len(L)-1):
    L2.append(L[i] + L[i + 1])

print(L2)
