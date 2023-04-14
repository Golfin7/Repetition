while True:
    nome = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if nome == senha:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Login realizado com sucesso!")
        break