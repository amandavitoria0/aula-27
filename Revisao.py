#LER ENTRADAS DO USUÀRIO
cont = 0 #variavel que controla a repetição
escolha_usuario = int(input()) #variavael que guarda quantas vezes o codigo vai rodar
while cont < escolha_usuario:
    nome = input()#ARMAZENAR o nome do aluno
    nota1 = float(input()) #4 notas do aluno
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())
    
    faltas = int(input())
    #CALCULO DA MEDIA
    media = (nota1+nota2+nota3+nota4)/4
    print(media)

    #LÓGICA DA SITUAÇÃO
    if faltas > 31:
        situacao = "Reprovado por falta"
    elif media >= 8:
        situacao = "Aprovado"
    elif media >= 5: #RECUPERAÇÃO
        recuperacao =float(input())#LER A NOTA DA PROVA DE RECUPERAÇÃO
        if recuperacao >= (10-media):
            situacao = "Aprovado na recuperação"
        else:
            situacao = "Reprovado na recuperação"
    else:
        situacao = "Reprovado por média"

        #RELATÓRIO
    print ("Nome:", nome)
    print ("Notas:",nota1, nota2, nota3, nota4)
    print("Faltas:",faltas)
    print("Média:",media)
    print("Recuperação:")
    cont = cont + 1




