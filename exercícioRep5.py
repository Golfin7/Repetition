while True:
    try:
        pop_a = int(input("Informe a população da cidade A: "))
        if pop_a < 0:
            print("A população deve ser um número positivo!")
            continue
        taxa_a = float(input("Informe a taxa de crescimento da cidade A em %: "))
        if taxa_a < 0:
            print("A taxa de crescimento deve ser um número positivo!")
            continue
        pop_b = int(input("Informe a população da cidade B: "))
        if pop_b < 0:
            print("A população deve ser um número positivo!")
            continue
        taxa_b = float(input("Informe a taxa de crescimento da cidade B em %: "))
        if taxa_b < 0:
            print("A taxa de crescimento deve ser um número positivo!")
            continue
        break
    except ValueError:
        print("Entrada inválida! Tente novamente.")

anos = 0
while pop_a < pop_b:
    anos += 1
    pop_a *= 1 + taxa_a/100
    pop_b *= 1 + taxa_b/100

print(f"Levará {anos} anos para a população da cidade A ultrapassar a população da cidade B.")
