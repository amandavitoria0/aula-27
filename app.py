#CADASTRO DE USUARIO E SENHA
#DECLARAR FUNÇÃO
def validar_senha (senha):
    senha_validar = input("digite sua senha")
    if senha_validar == senha:
      return True #Retorna verdadeiro

saldo = 0.0 #variavel que guardara o saldo do usuario
while True:
#MENU PRINCIPAL
    print("Bem vindo! \n digite 1.cadastrar 2.login 3.encerrar")

    #LER A ESCOLHA DO USUARIO
    escolha_menu = int(input()) #LE A ESCOLHA COM UM NUMERO

    #se o usuario escolher cadastro
    if escolha_menu == 1:
        #cria um usuario
        usuario = input("Crie um nome de usuario")
        senha = input("Crie uma senha")
    elif escolha_menu == 2: #SE USUARIO ESCOLHER LOGIN
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuario")
        login_senha = input("Digite sua senha")
        if login_usuario == usuario and login_senha == senha:
            print("Login realizado com sucesso")
            #SE LOGIN CORRETO, ENTRA NO
            #MENU PRINCIPAL DO APP
            while True: #ENQUANTO QUE EXIBIRA O MENU PRINCIPAL
                print("1.Deposito 2.Sacar 3.Pix 4.Extrato 5.Encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1:
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #ATUALIZA O VALOR
                elif escolha_principal == 2: #SAQUE
                    valor_saque = float(input("digite o valor do saque"))
                    if validar_senha():
                       saldo = saldo - valor_saque #subtrai o valor do saldo
                    else:
                        print("senha incorreta")
                elif escolha_principal == 3:
                    valor_pix = float (input("digite o valor do pix"))
                    if validar_senha():
                        saldo = saldo - valor_pix
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4: #se usuario escolher vizualizar
                    if validar_senha == senha:
                        print("extrato:", saldo)
                    else:
                        print("senha incorreta")
                elif escolha_principal == 5:
                     senha_encerrar = input("digite sua senha")
                     if senha_encerrar == senha:
                        break
                     else:
                         print("senha incorreta")
    else:
        print("usuario ou senha incorretos")
    