'''#INTERPOLAÇÕES DE VARIAVEIS; 

# EXISTEM 3 FORMAS DE UTILIZAR A INTERPOLAÇÕES DE VARIAVEIS; 
    1. % (não muito utilizada)
    2. format
    3. f strings'''

# PRIMEIRA FORMA (OLD STYLE) %

'''nome = "Erick Vinicius"
idade = 31 
profissao = "Programador"
linguagem = "Python"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem)) '''

# %s = formato string
# %d = formato int 
# %f = formato float
# --------------------------------------------------
# SEGUNDO FORMA METODO FORMAT {};
 
'''nome = "Erick Vinicius"
idade = 31 
profissao = "Programador"
linguagem = "Python"

print("Ola, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem)) '''

# TERCEIRA FORAM f-string (mais usado)

nome = "Erick Vinicius"
idade = 31 
profissao = "Programador"
linguagem = "Python"

print(f"Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.") 


# FORMATACAO STRINGS COM f-strings

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")