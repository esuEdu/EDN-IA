
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

try:
    ano_usuario = int(input("Digite um ano: "))
    if ano_usuario <= 0:
        print("Ano inválido. Por favor, insira um ano positivo.")
    else:
        if eh_bissexto(ano_usuario):
            print(f"O ano {ano_usuario} é bissexto.")
        else:
            print(f"O ano {ano_usuario} não é bissexto.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro para o ano.")
