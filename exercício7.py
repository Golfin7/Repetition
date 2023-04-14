numeros = []

for n in range(5):
    numero = int(input(f"Digite o {n+1}° número;"))
    numeros.append(numero)

soma = sum(numeros)
multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

print("Números digitados:", numeros)
print("Soma:", soma)
print("multiplicação:", multiplicacao)