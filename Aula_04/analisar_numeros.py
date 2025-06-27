
def analisar_numeros():
    """
    Analisa números, classificando-os como pares ou ímpares.
    """
    pares = 0
    impares = 0

    while True:
        try:
            num_str = input("Digite um número (ou 'fim' para terminar): ")
            if num_str.lower() == 'fim':
                break
            num = int(num_str)
            if num % 2 == 0:
                print(f"{num} é par.")
                pares += 1
            else:
                print(f"{num} é ímpar.")
                impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro ou 'fim'.")

    print("\n--- Resumo ---")
    print(f"Números pares inseridos: {pares}")
    print(f"Números ímpares inseridos: {impares}")

if __name__ == "__main__":
    analisar_numeros()

