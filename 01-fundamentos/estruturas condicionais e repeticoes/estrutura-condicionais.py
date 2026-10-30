'''
Percuso; 
    ETAPA 01 = 
        a. if
        b. if/else
        c. elif
    
    ETAPA 02 =
        a. if aninhado
    
    ETAPA 03 = 
        a. if ternário
'''

# IF = Estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões logicas são atendidas. 

'''saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")'''

# IF/ELSE = Estrutura condicional com dois desvio, podemos utilizar as palavras reservadas if e else. COmo sabemos se a expressao logica testada no IF for verdadera, então o bloco de codigo do IF será executado. Caso contrario o bloco de codigo do ELSE será executado.

'''saldo = 1200
saque = float(input("Informe o valor do saque: "))

if saque <= saldo:
    print("Saque realizado! Verifique seu e-mail")
else:
    print("Saldo insuficiente!")'''

# IF/ELIF/ELSE = Estrutura que em alguns cenários exige mais de dois desvios (elif), que será utilizando quando o primeiro bloco da condição (if) retorne verdadeiro.

'''opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato...")

else:
    sys.exit("Opção Invalida")'''

