#
#Autor - maahzodd
#
#WLgen.py - cria uma wordlist que pode ser usada em bruteforce
#
# v1.0 2024-11-23, maahzodd:
#   -sou iniciante estou melhorando
#
from pathlib import Path

#escolha de nome e procedimento padrao
wl_nome = input("qual o nome da wordlist?: ")+".txt".lower().strip()
dicionario = Path(wl_nome)
if not dicionario.exists():
    dicionario.touch()

#coleta de dados e escolhas
nome = input("nome: ").strip()
snome = input("sobrenome: ").strip()
nick = input("apelido: ").strip()
birth = input("data de nascimento(DDMMAAAA): ").strip()
palavras_chave = input("adicionar palavras-chave?(S/N): ").lower()
if palavras_chave == "s":
    key = input("adicione as palavras-chave separadas por virgula: ").split(",")
anos = input("combinar com anos(2000,2024)?(S/N): ").lower()
ordem = input("escolher ordem de escrita?(S/N): ").lower()
if ordem == "s":
    order = input("escolha a ordem:\n[1]---basica | [2]---chaves | [3]---anos\n\
separados por virgula: ").split(",")

#STRING QUE SERA ESCRITA NO ARQUIVO
STRING = ""

#funcoes

##essa funcao sera usada dentro das outras para fazer a ordem funcionar
def combina(x,y,repete="s"):
    global STRING
    if x!="" and y!="" and x!=y and repete=="s":
        STRING += f"{x}{y}\n{y}{x}\n"
    elif x!="" and y!="" and x!=y:
        STRING += f"{x}{y}\n"

##funcoes compostas, feitas assim para fazer a escolha da ordem funcionar
def Basica():
    global STRING
    combina(nome,snome);combina(nome,nick);combina(snome,nick)
    STRING+=f"{birth}\n"

def Chaves():
    if palavras_chave=="s":
        for x in key:
            combina(x,nome)
        for x in key:
            for y in key[::-1]:
                combina(x,y,"n")
def Anos():
    if anos == "s":
        for year in range(2000,2025):
            combina(nome,year,"n");combina(snome,year,"n");combina(nick,year,"n")
            combina(year,nome,"n");combina(year,snome,"n");combina(year,nick,"n")
        if palavras_chave == "s":
            for x in key:
                for year in range(2000,2025):
                    combina(x,year,"n");combina(year,x,"n")

#ORDEM EXECUCAO
dicio = {"1":"Basica()","2":"Chaves()","3":"Anos()"}
if ordem == "s":
    for x in order:
        exec(dicio[x])
else:
    Basica();Chaves();Anos()

#ESCRITA
dicionario.write_text(STRING)
print("\n"*99)
print(f"{wl_nome} foi criado com sucesso!!!")
