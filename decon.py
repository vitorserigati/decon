from tkinter import * #importação da biblioteca 'tkinter', nativa do python

janela = Tk() #instanciação da biblioteca como janela
janela.title("Projeto Interdisciplinar") #nome da janela
janela.geometry("500x500") #tamanho da janela
janela.resizable(False, False) #torna o tamanho da janela fixa. (Não se pode aumentar ou diminuir)


def converter_binario(): #criação da função que converterá em binários
    numero = int(dado_usuario.get()) #recebe o número digitado pelo usuário, e armazena na variável 'numero'

    sequencia="" #inicia uma variável str vazia
    valorcont = numero #inicia a variavel de contagem, com o valor digitado pelo usuário
    while(valorcont>0): #estrutura que repetirá o código, até que o valor chegue a 0
        resto = valorcont%2 #armazena o resto da divisão do valor dividido por 2
        sequencia += str(resto) #atribui a sequencia já existente com o resto
        valorcont=valorcont//2 #divide o valor da contagem por 2 e armazena o resultado como inteiro
        resultadof=sequencia[::-1] #inverte a sequência e armazena no resultado


    resultado = Label(janela, text=("Resultado: "+ resultadof), width=50)  #instancia uma 'label' (texto) com o resultado da função
    resultado.place(x=70, y=250) #adiciona o texto à janela, na posição indicada

def converter_hexa(): #criação da função que converterá em hexadecimal
    numero=int(dado_usuario.get())
    sequencia = ''
    valorcont = numero
    while (valorcont > 0):

        if (valorcont % 16 == 10):  # verifica se o valor é igual a 10
            resto = 'A'  # caso o valor seja igual a 10, atribui a letra A ao resto
        elif (valorcont % 16 == 11): # verifica se o valor é igual a 11
            resto = 'B'  # caso o valor seja igual a 11, atribui a letra B ao resto
        elif (valorcont % 16 == 12): # verifica se o valor é igual a 12
            resto = 'C'  # caso o valor seja igual a 12, atribui a letra C ao resto
        elif (valorcont % 16 == 13): # verifica se o valor é igual a 13
            resto = 'D'  # caso o valor seja igual a 13, atribui a letra D ao resto
        elif (valorcont % 16 == 14): # verifica se o valor é igual a 14
            resto = 'E'  # caso o valor seja igual a 14, atribui a letra E ao resto
        elif (valorcont % 16 == 15): # verifica se o valor é igual a 15
            resto = 'F'  # caso o valor seja igual a 15, atribui a letra F ao resto
        else:
            resto = valorcont % 16 #armazena o resto da divisão do valor dividido por 16
        sequencia += str(resto)
        valorcont = valorcont // 16 #divide o valor da contagem por 16 e armazena o resultado como inteiro
        resultadof = sequencia[::-1]

        resultado = Label(janela, text=("Resultado: "+ resultadof), width=50) #instancia uma 'label' (texto) com o resultado da função
        resultado.place(x=70, y=250)  #adiciona o texto à janela, na posição indicada

def converter_octa(): #criação da função que converterá em octal
    numero=int(dado_usuario.get())
    sequencia = ''
    valorcont = numero
    while (valorcont > 0):
        resto = valorcont % 8 #armazena o resto da divisão do valor dividido por 8
        sequencia += str(resto)
        valorcont = valorcont // 8 #divide o valor da contagem por 16 e armazena o resultado como inteiro
        resultadof = sequencia[::-1]

        resultado = Label(janela, text=("Resultado: "+ resultadof), width=50) #instancia uma 'label' (texto) com o resultado da função
        resultado.place(x=70, y=250)  #adiciona o texto à janela, na posição indicada


label=Label(text="Digite o número decimal", width=50) #Criação do texto (label) para informar ao usuário digitar um número
label.place(x=65, y=20)  #adiciona a label à janela na posição informada

dado_usuario=Entry(width=25,justify="left", font="Arial") #Criação de uma janela para o usuário digitar um valor
dado_usuario.place(x=130, y=50) #posicionamento da janela de input do usuário

botao_binario=Button(janela, text="Conversão para Binário", width=20, command=converter_binario) #criação do botão de conversão para binário. 'Command' chamará a função criada anteriormente
botao_binario.place(x=165, y=100) #posicionamento do botão binário

botao_hexadecimal=Button(janela, text="Conversão para Hexadecimal", width=25, command=converter_hexa) #criação do botão de conversão para headecimal. 'Command' chamará a função criada anteriormente
botao_hexadecimal.place(x=145, y=150) #posicionamento do botão hexadecimal

botao_octa=Button(janela, text="Conversão para Octa", width=20, command=converter_octa) #criação do botão de conversão para octal. 'Command' chamará a função criada anteriormente
botao_octa.place(x=165, y=200) #posicionamento do botão octa


#Nome e RGM dos alunos
label1=Label(text="Alisson Cavalcante da Silva RGM - 29431824")
label1.place(x=30, y=330)

label2=Label(text="Danilo Paz RGM - 30357136")
label2.place(x=30, y=360)

label3=Label(text="Henrique Serigati de Oliveira Basso RGM - ")
label3.place(x=30, y=390)

label4=Label(text="Vitor Serigati de Oliveira Basso RGM - 30348820")
label4.place(x=30, y=420)

label5=Label(text="Projeto Interdisciplinar - Universidade Cruzeiro do Sul")
label5.place(x=30, y=450)

janela.mainloop() # faz com que a janela continue aberta, até que se precione o X para fechar