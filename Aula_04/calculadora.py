
def calculadora():
    """
    Uma calculadora simples que realiza as quatro operações básicas.
    """
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite a sua escolha(1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")
                continue

            if escolha == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif escolha == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif escolha == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif escolha == '4':
                if num2 == 0:
                    print("Erro! Divisão por zero.")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
            
            proxima_calculo = input("Deseja fazer outro cálculo? (sim/não): ")
            if proxima_calculo.lower() != 'sim':
                break
        else:
            print("Entrada inválida. Por favor, selecione uma opção de 1 a 4.")

if __name__ == "__main__":
    calculadora()
