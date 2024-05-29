import os
def stampamenu():
    print("1) aggiungi un nuovo articolo alla lista")
    print("2) eliminare uno specifico articolo dalla lista")
    print("3) visualizzare l'elenco degli articoli presenti nella lista")
    print("4) esci")

def scelta():
    scelte_possibili = ("1","2","3","0")
    errore = True
    while errore:
        errore = False
        scelta = input("Fai la tua scelta: ")
        if scelta not in scelte_possibili:
            errore = True
            print("Scelta non accettabile")
        else:
            errore = False
            return scelta

def aggiungi(lista,ciao):
    coso = input("Inserisci un elemento da aggiungere alla lista: ")
    errore = True
    while errore:
        if coso == " ":
            errore = True
            print("Non puoi aggiungere il vuoto")
        else:
            errore = False
            lista.append(coso)
        
    salva(lista,ciao)

def elimina(lista,nome):
    print(lista)
    errore = True
    while errore:
        errore = False
        coso = input("Inserisci un elemento da eliminare: ")
        if coso not in lista:
            print("elemeno non presente in lista")
            errore = True
        else:
            errore = False
            lista.remove(coso)
    salva(lista,nome)


def visualizza(lista):
    for i in range(len(lista)):
        print(f"elemento numero {i}: {lista[i]}")

def salva(lista,nome):
    f = open(nome,"w")
    for i in lista:
        f.write(i + "\n") 
    f.close()

def carica(lista):
    percorso = os.getcwd()
    lista1 = os.listdir(percorso)
    print(lista1)
    errore = True
    while errore:
        errore = False
        nomefile2 = input("Inserisci il nome del file da caricare: ")
        f = open(nomefile2,"r")
        for i in f:
            lista.append(i)
        return nomefile2




lista_principale = []
nomde_file = carica(lista_principale)


s = ""
while s != "0":
    stampamenu()
    s = scelta()

    match s:
        case "1":
            aggiungi(lista_principale,nomde_file)
        case "2":
            elimina(lista_principale,nomde_file)
        case "3":
            visualizza(lista_principale)
        case "4":
            quit()