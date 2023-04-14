V1 = [1,3,5,7,9,11,13,15,17,19]
V2 = [2,4,6,8,10,12,14,16,18,20]
V3 = []

contador = 0
for n in V1:
    V3.append(n)
    V3.append(V2[contador])
    contador += 1
print("Números intercalados entre os vetores")
print(V3)