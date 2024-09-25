nota_alunos = {}
erro = ""
contador = 5

while contador > 0:
    print(erro)
    nome = input("digite o nome do aluno: ").strip().capitalize()
    input_nota1 = input("digite a primeira nota: ").replace(",", ".")
    input_nota2 = input("digite a segunda nota nota: ").replace(",", ".")
    input_nota3 = input("digite a primeira nota: ").replace(",", ".")

    if not nome:
        erro = "!o aluno precisa de um nome!"
        continue
    else:
        nota1 = int(input_nota1)
        nota2 = int(input_nota2)
        nota3 = int(input_nota3)
        media = (nota1 + nota2 + nota3) / 3
        nota_alunos[nome] = {"media": media}
        contador -= 1 

for aluno, valor in nota_alunos.items:
    print(f"o aluno {aluno} eta com media {valor[media]}")