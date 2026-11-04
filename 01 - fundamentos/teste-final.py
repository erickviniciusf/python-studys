# Solicita ao usuário um número inteiro
numero = int(input())

# TODO: Verifique se o número é par ou ímpar e imprima o resultado:

if (numero % 2) == 1:
    print("Ímpar")
else:
    print("Par")    

# ----------------------------------------------

def verificador_ano_bissexto():
    ano = int(input())
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

verificador_ano_bissexto()
#-----------------------------------------------

def conta_vogais(texto):
    VOGAIS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    contador = 0
    for char in texto:
        if char in VOGAIS:
          contador += 1
    return contador

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")