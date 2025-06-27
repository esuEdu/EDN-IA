import string

def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

