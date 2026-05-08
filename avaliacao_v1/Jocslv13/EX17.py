# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Classificação por faixas etárias
if idade < 18:
    print("Classificação: Menor de idade.")
elif 18 <= idade <= 59:
    print("Classificação: Maior de idade.")
else:
    print("Classificação: Idoso.")