#DECLARAR AS FUNÇÃO
def saudacoes(hora_do_dia): #Exibir a saudação correspondente a hora do dia
  #CONDIÇÃO PARA DAR BOM DIA  
    if (hora_do_dia >=0) and (hora_do_dia <= 12):
        print("BOM DIA!!!!")
        #CONDIÇÃO PARA DAR BOA TARDE
    elif (hora_do_dia >= 13 and (hora_do_dia <= 18)):
        print("boa tarde!")
    elif (hora_do_dia >= 19 and (hora_do_dia <= 23)):
        print("BOA NOITE!")

#FORA DA FUNÇÃO
#peço para o usuario dizer a hora atual
resposta = int(input("Digite que horas sao:\n"))
#CHAMO A FUNÇÃO PASSANDO PARA ELA O PARAMETRO OBRIGATORIO
saudacoes(resposta)