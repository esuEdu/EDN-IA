from datetime import datetime

def calcular_dias_de_vida():
    data_nasc_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y")
    hoje = datetime.today()

    dias_vividos = (hoje - data_nasc).days
    print(f"Você está vivo há {dias_vividos} dias.")

