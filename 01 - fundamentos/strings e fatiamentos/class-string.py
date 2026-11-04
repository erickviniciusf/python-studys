# METODOS UTEIS DA CLASSE STRING

curso = "pYtHoN"

print(curso.upper()) #Deixa toda a palavra com letras maisculas

print(curso.lower()) #Deixa toda a palavra com letra minusculas

print(curso.title()) #Deixa a primeira letra da palavra maiuscula, tipo Titulo


curso2 = "   Python "

print(curso2.strip()) #remove todos os espaços de ambos os lados 

print(curso2.lstrip()) #remove os espaços do lado esquerdo

print(curso2.rstrip()) #remove os espaços do lado direito


curso3 = "Python"

print(curso3.center(10, "#")) #no primeiro argumento fornece quantos caracteres voce quer na saida, e o segundo argumento é opcional que é o caractere que voce quer nesses espaços

print(".".join(curso3)) #funciona todo tipo iteravel também, ele coloca o caracter que voce colocou na instrução a cada letra.
