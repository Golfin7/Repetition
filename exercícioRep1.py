while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota < 0 or nota > 10:
        print("Valor inválido. A nota deve ser entre zero e dez.")
    else:
        break

print("A nota digitada foi:", nota)