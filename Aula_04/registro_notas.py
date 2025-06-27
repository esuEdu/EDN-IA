# Dicionário para armazenar os alunos e suas notas
alunos = {}

# Pergunta quantos alunos serão registrados
quantidade = int(input("Quantos alunos deseja registrar? "))

# Loop para registrar cada aluno
for _ in range(quantidade):
    nome = input("\nNome do aluno: ")
    notas = []
    
    # Coleta 3 notas por aluno (pode mudar se quiser mais ou menos)
    for i in range(1, 4):
        nota = float(input(f"Nota {i} de {nome}: "))
        notas.append(nota)
    
    # Armazena no dicionário
    alunos[nome] = notas

# Agora vamos calcular as médias
soma_das_medias = 0

print("\n Médias dos alunos:")
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    soma_das_medias += media
    print(f"{nome}: média = {media:.2f}")

# Média da turma
media_geral = soma_das_medias / len(alunos)
print(f"\nMédia geral da turma: {media_geral:.2f}")

