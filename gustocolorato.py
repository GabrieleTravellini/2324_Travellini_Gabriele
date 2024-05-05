import colored
lista = []

def carica(lista):
    s = open("gusti2.txt", "r")
    for i in s:
            lista.append(i.strip())

carica(lista)


gusti_colorati = []

def creatupla(lista):
    for i in range(0, len(lista), 2):
        gusto = lista[i]
        colore = lista[i+1]
        gusti_colorati.append((gusto, colore))

creatupla(lista)

def coloratupla(gusti_colorati):
    for gusto, colore in gusti_colorati:
        gusto_colorato = colored.fg(colore) + gusto 
        print(gusto_colorato)

coloratupla(gusti_colorati)