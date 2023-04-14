U = []

for n in range (10):
    numero = int(input(f"Digite o {n+1}° número:"))
U.append(numero)

soma = sum(U)  
multiplicação = 1
for numero in U:
    multiplicação *= numero
print("soma dos números:")
print(soma)
print("número da soma ao quadrado:")
print(multiplicação)