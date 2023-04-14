numeros = []
soma = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma += numero

media = soma / len(numeros)
print("A soma dos números é:", soma)
print("A média dos números é:", media)