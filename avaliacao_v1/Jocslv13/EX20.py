# Inicializa o contador antes do laço
contador_positivos = 0

print("Por favor, digite 10 números:")

# O laço for repetirá 10 vezes
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    # Verifica se o número digitado é positivo
    if numero > 0:
        contador_positivos += 1

# Exibe o resultado final
print("-" * 30)
print(f"Total de números positivos digitados: {contador_positivos}")