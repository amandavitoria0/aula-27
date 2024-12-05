#LER ENTRADAS DO USUÀRIO
escolha_menu = int(input("escolha opcao"))#variavel que guarda a escolha do usuario
if escolha_menu == 1: #se a escolha for para realizar u
    aluno = [] #lista que guarda56todos os alunos cadastrar
    cont = 0 #variavel que controla a repetição
    escolha_usuario = int(input("digite quantos alunos deseja cadastrar")) #variavael que guarda quantas vezes o codigo vai rodar
    while cont < escolha_usuario:
        nome = input("digite o nome do aluno")#ARMAZENAR o nome do aluno
        nota1 = float(input("digite a primeira nota:")) #ler as notas
        nota2 = float(input("digite a segunda nota:")) #ler as notas
        nota3 = float(input("digite a terceira nota:")) #ler as notas
        nota4 = float(input("digitea quarta nota:")) #ler as notas
        
        faltas = int(input("digite a quantidade de faltas:"))
        #CALCULO DA MEDIA
        media = (nota1+nota2+nota3+nota4)/4
        #LÓGICA DA SITUAÇÃO
        if faltas >= 31:
            situacao = "Reprovado por falta"
        elif media >= 8:
            situacao = "Aprovado"
        elif media >= 5: #RECUPERAÇÃO
            recuperacao =float(input("digite a nota da recuperação:"))#LER A NOTA DA PROVA DE RECUPERAÇÃO
            if recuperacao >= (10-media):
                situacao = "Aprovado na recuperação"
            else:
                situacao = "Reprovado na recuperação"
        else:
            situacao = "Reprovado por média"
            #enviar os dados do aluno para a lista alunos
            aluno.append([nome, faltas, media, situacao])
            cont += 1
        #relatório
        print(aluno)




