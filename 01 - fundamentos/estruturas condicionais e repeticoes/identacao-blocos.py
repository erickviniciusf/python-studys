#Identação e os blocos de comando

#A identação do codigo é uma forma de manter o codigo fonte mais legivel e manutenivel. Sem contar que é uma forma de deixar explicito onde o codigo comeca e onde termina 

# Blocos de comandos 

#É indicado que em python utilize 4 espaços em branco por nivel de identação, ou seja, a cada novo bloco adicionamos 4 novos espacos em branco. 

'''def sacar(self, valor: float) -> None: 
    if self.saldo >= valor:
        self.saldo -= valor
'''
# o que não funciona em python; 

'''def sacar(self, valor: float) -> None:
if self.saldo >= valor:
self.saldo -= valor'''

#EXEMPLOS

def sacar(valor):
    saldo = 3000

    if saldo >= valor:
        print("Valor sacado!")
    else:
        print("Valor não sacado")


sacar(10000)