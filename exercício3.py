exercici03 = [10, 9.0, 8.0, 7.0]
media = 0
for i in range (0, len(exercici03)):
    print("nota", i+1, ":", exercici03[i])
    media = media + exercici03[i]
media = media / len(exercici03)
print("média:", media)