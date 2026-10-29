# OPERADORES LOGICOS 
# SÃO OPERADORES UTILIZADOS EM CONJUNTOS COM OS OPERADOREDORES DE COMPARAÇÕES

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
print(saque <= limite)

#OPERADOR "E" >> "end" SE ALGUMA DAS PARTES FOR FALSE A RESPOSTA SEMPRE SERÁ FALSE

print(saldo >= saque and saque <= limite) 
# saldo é maior ou igual a saque? SIM
# saque é menor ou igual a limite? NÃO
# Então o valor é false, pois uma das partes foi negativa; relação = true + false = false or false + true = false

#OPERADOR "OU" >> "or" SE ALGUMA DAS PARTES FOR TRUE A RESPOSTA SEMPRE SERÁ TRUE

print(saldo >= saque or saque <= limite)
# saldo é maior ou igual a saque? SIM
# saque é menor ou igual a limite? NÃO
# Então o valor é true, pois uma das partes foi positiva; relação = true + false = true or false + true = true

#OPERADOR NEGAÇÃO 

contato_emergencia = []

print(not 1000 > 1500)
#O resultado sai true porque 1000 é menor que 1500 porem como o resultado da comparação é realizada primeiro, a negação pela o resultado da comparação e inverte, o que é true vira false e o que é false vira true.

print(not contato_emergencia)
#Mesma coisa, lista em py vazia é false, como tem o operador negação (not) em frente a variavel, ela vira true.

print(not "saque 1500;")
#Aqui no caso string é true, porem como existe o not em frente se torna false

print(not "")
#String vazia é false, logo, com o not vira true