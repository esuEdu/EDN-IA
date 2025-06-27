
def classificar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

try:
    idade_usuario = int(input("Digite sua idade: "))
    if idade_usuario < 0:
        print("Idade inválida. Por favor, insira um número positivo.")
    else:
        categoria = classificar_idade(idade_usuario)
        print(f"Você é classificado como: {categoria}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
