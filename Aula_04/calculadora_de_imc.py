
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

try:
    peso_usuario = float(input("Digite seu peso em kg: "))
    altura_usuario = float(input("Digite sua altura em metros: "))
    
    if peso_usuario <= 0 or altura_usuario <= 0:
        print("Valores de peso e altura devem ser positivos.")
    else:
        imc_calculado = calcular_imc(peso_usuario, altura_usuario)
        categoria_imc = classificar_imc(imc_calculado)
        print(f"Seu IMC é: {imc_calculado:.2f}")
        print(f"Classificação: {categoria_imc}")
except ValueError:
    print("Entrada inválida. Por favor, insira números.")
