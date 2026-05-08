# O range vai de 1 até 20 (o 21 é o limite exclusivo)
for numero in range(1, 21):
    # Verifica se o resto da divisão por 2 é zero
    if numero % 2 == 0:
        print(f"O número {numero} é PAR")
    else:
        print(f"O número {numero} é ÍMPAR")