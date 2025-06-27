def calcular_preco_com_desconto():
    preco = float(input("Digite o preço original do produto: R$ "))
    desconto = float(input("Digite a porcentagem de desconto: "))

    valor_desconto = preco * (desconto / 100)
    preco_final = round(preco - valor_desconto, 2)

    print(f"Preço final com desconto: R$ {preco_final}")

