# EXEMPLO DE ESTRUTURA DE REPETIÇÃO SEM REPETIÇÃO 

'''a = int(input("Informe um numero inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)'''

# COMANDO 'FOR' é usado para percorrer um objeto iteravel. 

'''texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS: #upper transforma de minusculo para maiusculo
        print(letra, end="")

print()'''

# FUNCAO range = é usado para produzir uma sequencia de numeros inteiros a partir deu m inicio (inclusivo) para um fim (exclusivo)
# ELA RECEBE 3 ARGUMENTOS: STOP, START, STEP

'''for numero in range(0, 11): # ele devolve uma lista do 0 a 10
    print(numero, end=" ")

print()

for numero in range(0, 50, 2): #o ultimo digito informa a quantidade de pulos que a lista vai ter, ex atual é o 2, entaõ a cada 2 numeros ele informa 1
    print(numero, end=" ") # o END é opcional é apenas para deixar em formato de lista, um ao lado do outro. '''


# COMANDO WHILE 

# COMANDO WHILE É UTILIZADO QUANDO NAO SABEMOS QUANTAS VEZES TERÁ QUE REPETIR. 
'''
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    else:
        print("Obrigado por utilizar o sistema! ")'''

'''for numero1 in range(100):
    if numero1 == 29:
        break #quando chegar no numero 29 o programa para! 

    print(numero1, end=" ")


for numero2 in range(100):
    if numero2 == 12:
        continue #quando chegar em 11 ele pula o 12 e o programa continua até o final do range

    print(numero2, end=" ")
'''

# FAÇA UM PROGRAMA QUE MOSTRE SOMENTE OS NUMEROS IMPARES DE 0 A 100; 

for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end=" ")

# FACA UM PROGRAMA QUE MOSTRE SOMENTE OS NUMEROS PARES DE 0 A 100; 

for numero in range(0, 100, 2):
    print(numero, end =" ")