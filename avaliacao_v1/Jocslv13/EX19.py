# Inicializamos a variável antes do laço para que a condição possa ser testada
senha = ""

# O loop continuará rodando enquanto a senha for diferente de "acesso"
while senha != "acesso":
    senha = input("Digite a senha: ")

    if senha == "acesso":
        print("Senha correta! Bem-vindo ao sistema.")
    else:
        print("Senha incorreta. Tente novamente.")