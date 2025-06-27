
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

try:
    temp = float(input("Digite a temperatura: "))
    unidade_origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    unidade_destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    resultado = 0
    if unidade_origem == "celsius":
        if unidade_destino == "fahrenheit":
            resultado = celsius_para_fahrenheit(temp)
        elif unidade_destino == "kelvin":
            resultado = celsius_para_kelvin(temp)
        else:
            resultado = temp 
    elif unidade_origem == "fahrenheit":
        if unidade_destino == "celsius":
            resultado = fahrenheit_para_celsius(temp)
        elif unidade_destino == "kelvin":
            resultado = fahrenheit_para_kelvin(temp)
        else:
            resultado = temp
    elif unidade_origem == "kelvin":
        if unidade_destino == "celsius":
            resultado = kelvin_para_celsius(temp)
        elif unidade_destino == "fahrenheit":
            resultado = kelvin_para_fahrenheit(temp)
        else:
            resultado = temp
    else:
        print("Unidade de origem inválida.")

    if resultado:
      print(f"{temp}° {unidade_origem.capitalize()} é igual a {resultado:.2f}° {unidade_destino.capitalize()}")

except ValueError:
    print("Entrada de temperatura inválida. Por favor, insira um número.")
