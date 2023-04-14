V1 = [1,4,7,10,13,16,19,22,25,28]
V2 = [2,5,8,11,14,17,20,23,26,29]
V3 = [3,6,9,12,15,18,21,24,27,30]
V4 = []

contador = 0
for n in V1:
    V4.append(n)
    V4.append(V2[contador])
    V4.append(V3[contador])
    contador += 1
print("Números intercalados entre os vetores")
print(V4)