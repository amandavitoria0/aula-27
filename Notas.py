
quantAluno = int(input("Digite a quantidade de alunos:"))

quantFaltas = int(input("Digite  número de faltas:"))

print("Digite o nome do aluno:")
nome = (input())

print("Digite a nota 1:")
nota1 = float(input())
print("Digite a nota 2:")
nota2 = float(input())
print("Digite a nota 3:")
nota3 = float(input())
print("Digite a nota 4:")
nota4 = float(input())

media = (nota1 + nota2 + nota3 + nota4)/4 

print("A média do", nome, "é:", media)


if media >=8:
   print("APROVADO")
else:
    print("REPROVADO por média")

if (media >=5):
   print("o aluno não precisa realizar a recuperação. Sua média é:",media)
else:
   print("REPROVADO, pois não foi permitido fazer a recuperação")







