
def verificar_senha():
    """
    Verifica se a senha atende aos critérios básicos de segurança.
    """
    while True:
        senha = input("Digite a sua senha: ")
        
        tem_oito_caracteres = len(senha) >= 8
        tem_numero = any(char.isdigit() for char in senha)

        if tem_oito_caracteres and tem_numero:
            print("Senha válida!")
            break
        else:
            print("Senha inválida. Verifique os critérios:")
            if not tem_oito_caracteres:
                print("- Deve ter pelo menos 8 caracteres.")
            if not tem_numero:
                print("- Deve conter pelo menos um número.")

if __name__ == "__main__":
    verificar_senha()
