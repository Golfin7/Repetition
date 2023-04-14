idade = [66, 78, 88, 77, 20]
altura = [1.56, 1.9, 1.8, 1.2, 1.3]
altura0 = []
idade0 = []

print(idade)
print(altura)

for n in range (5):
    idade0.append(idade.pop())
    altura0.append(altura.pop())

print(idade0)
print(altura0)