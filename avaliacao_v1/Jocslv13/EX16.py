# Solicita a entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Estrutura de decisão para verificar a faixa do número
if numero > 0:
    print(f"O número {numero} é POSITIVO.")
elif numero < 0:
    print(f"O número {numero} é NEGATIVO.")
else:
    print("O número é ZERO.")