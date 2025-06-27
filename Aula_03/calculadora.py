def calculadora():
    resultado = 0
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            
            operador = input("Digite a operação (+, -, *, /): ")

            if operador not in ['+', '-', '*', '/']:
                print("Operador inválido. Encerrando a calculadora.")
                continue

            num2 = float(input("Digite o segundo número: "))
            
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2

            print(f"Resultado: {num1} {operador} {num2} = {resultado}\n")
            break

        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.\n")

calculadora()
