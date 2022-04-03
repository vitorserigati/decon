def calculator(opcao, valor): #Criação da Função para o cálculo, com a opção escolhida e valor informados
    resultado = ''  #Resultado final das contas
    if (opcao == 1):    #verifica a opção. Se for igual a 1, realizará a covnersão para binário
        print("Você escolheu a conversão para binário: ")
        sequencia = '' #sequencia recebida das contas
        valorcont = valor #atribuição do valor recebido à variável usada no looping
        resto = 0  
        while (valorcont > 0): #enquanto o valor da conta for maior que 0 a operação se repete
            resto = valorcont%2 #atribui o resto da conta à variável resto 
            sequencia += str(resto) #transforma a variável resto em string, enquanto concatena com o valor anterior
            valorcont = valorcont//2 #Reatribui o valor de contagem com o resultado da divisão pela base (arredondado)
            resultado = sequencia[::-1] #atribui a sequencia de forma invertida ao resultado final
    elif (opcao == 2):  #verifica a opção. Se for igual a 2, realizará a covnersão para hexadecimal
        print("Você escolheu a conversão para hexadecimal: ")
        sequencia = ''
        valorcont = valor
        resto = 0
        while (valorcont > 0):
            
            if (valorcont%16 == 10): #verifica se o valor é igual a 10
                resto = 'A' #caso o valor seja igual a 10, atribui a letra A ao resto
            elif (valorcont%16 == 11):
                resto = 'B'
            elif (valorcont%16 == 12):
                resto = 'C'
            elif (valorcont%16 == 13):
                resto = 'D'
            elif (valorcont%16 == 14):
                resto = 'E'
            elif (valorcont%16 == 15):
                resto = 'F'
            else:
                resto = valorcont%16
            sequencia += str(resto)
            valorcont = valorcont//16
            resultado = sequencia[::-1]
    elif(opcao == 3):   #verifica a opção. Se for igual a 3, realizará a covnersão para octal
        print("Você escolheu a conversão para Octal: ")
        sequencia = ''
        valorcont = valor
        resto = 0
        while(valorcont > 0):
            resto = valorcont%8
            sequencia += str(resto)
            valorcont = valorcont//8
            resultado = sequencia [::-1]
    return f'O resultado da conversão é: {resultado}'   #retorna o resultado da função.

#Início da interação com o Usuário

print('Escolha uma opção: \n[1] = Conversor de Decimal para binário: \n[2] = Conversor de Decimal para Hexadecimal: \n[3] = Conversor de Decimal para Octal: ')
opcao = int(input())#atribuição da opção escolhida à variável
valor = int(input('Digite o valor que deseja converter: ')) #valor escolhido é digitado e guardado
print(calculator(opcao,valor)) #imprime o resultado da função com os argumentos escolhidos

