print("Olá, eu sou uma versão 'crua' da IA do meu mestre MAURICIO!")
print("Irei fazer algumas perguntas e gostaria que me responde-se. OK?")
print("APERTE ENTER PARA CONTINUAR!")
input("")

nome = input("Digite seu nome: ")
peso = input("E seu peso: ")

print("Agora vamos ver sua data de nascimento! OK?")
input("Aperte enter!")

dia = input("Dia: ")
mes = input("Mês: ")
ano = int(input("Ano: "))
anoatual = int(input("Qual ano voce se encontra?"))

print("PRONTO!")
print("Você nasceu dia:  {}/ {} / {} Neste dia você presenteou o MUNDO com sua pessoa!".format(dia, mes, ano))
print("obrigado!")

n2 = anoatual - ano

print("Se sua idade for correspondente a {} APERTE ENTER!".format(n2))
input("")
print("PRONTO! SEU CADASTRO FOI CONCLUIDO!")

#


print("DADOS PARA PROGRAMADOR!")

print("VARIAVEL|Ltr.MAIUSCULA|Ltr.MINUSCULA|NUMERO|ALPHANUMERICO")
print("NOME:|", nome.isupper(), "|", nome.islower(), "|", nome.isnumeric(), "|", nome.isalnum())
print("PESO:|", peso.isupper(), "|", peso.islower(), "|", peso.isnumeric(), "|", peso.isalnum())
print("DIA:|", dia.isupper(), "|", dia.islower(), "|", dia.isnumeric(), "|", dia.isalnum())
print("MES:|", mes.isupper(), "|", mes.islower(), "|", mes.isnumeric(), "|", mes.isalnum())

# OPERADORES ARITMETICOS:
#
# ( + ) ADIÇÃO
# ( - ) SUBTRAÇÃO
# ( * ) MULTIPLICAÇÃO
# ( / ) DIVISÃO
# ( ** ) POTÊNCIAÇÃO
# ( // ) DIVISÃO INTEIRA
# ( % ) RESTO DA DIVISÃO
# ( == ) IGUAL
#
# EXEMPLOS:
#
# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 2
# 5%2 == 1
# ordem de procedencia:
#
# 1º ()
# 2º **
# 3º * , / , // , %
# 4º + , -
#
#
#
# MAIS EXEMPLOS:
#
# 5+3*2 == 11
#
# 3*5+4**2==31
#
# 3*(5+4)**2==241
