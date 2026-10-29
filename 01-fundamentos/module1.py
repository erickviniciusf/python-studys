'''#VARIAVEIS E CONSTANTES 

nome = "Erick"
idade = 31


nome = "Giovanna"

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

print(BRAZILIAN_STATES)

'''

'''item = "Crepe"
quantidade = 3
preco = 12.5

print(f"{quantidade}x {item} = R${preco * quantidade:.2f}")
'''
'''
print(int(1.0))
print(str(10.10))
print(float(1.0323223))'''

#FUNCOES DE ENTRADA E SAIDA


#FUNÇÃO INPUT
    # É usado quando queremos ler dados da entrada padrão (teclado >> recebe um argumento do tipo string 

#nome = input("Informe o seu nome: ")

#FUNÇÃO PRINT 
    # É usado quando queremos exibir dados na saida padrão (tela) >> recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos argumentos opcionais (sep, end, file e flush)

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade ")

print(f"{nome}, Seja bem vindo ao MasterClass DIO. Vi que voce tem {idade} anos, pode seguir")