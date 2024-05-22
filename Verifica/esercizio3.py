import random
from termcolor import colored 

def carica(lista):
    try:
        f = open("frasi.txt","r")
        for i in f:
            i = i.strip("\n")
            lista.append(i)
    except:
        print("Il file non esiste")

def stampamenu():
    print("1) crea i giocatori")
    print("2) ")
    print("3) ")
    print("4) ")
    print("5) ")
    print("6) ")

def scelta(a):
    errore = True
    while errore:
        errore = False
        if len(a) > 1:
            errore = True
            if a not in "123456":
                errore = True
        else:
            errore = False
            return a

def crea_giocatori(lista):
    errore = True
    numero = int(input("Quanti giocatori giocano?"))
    lista_colori=["red","yellow","green","pink","blue"]
    while errore:
        errore = False
        for i in range(numero):
            print(lista_colori)
            b = input("Inserisci un colore: ")
            if b not in lista_colori:
                errore = True
                print("Colore non presente")
            else:
                errore = False
                ciao = input(colored("Inserisci il nickname del giocatore: "))
                nomegiocatore = ciao
                lista.append(nomegiocatore)

def gioco(lista,lista2):
    a = random.sample(lista,1)
    b = random.sample(lista2,1)
    c = "#"*len(a)
    print(f"E' il turno di: {b}")
    print(f"La frase nascosta è: {c}")

lista_frasi = []
lista_giocatori = []
carica(lista_frasi)

s = ""
while s != "6":
    stampamenu()
    a = input("Fai la tua scelta: ")
    s = scelta(a)
    match s:
        case "1":
            crea_giocatori(lista_giocatori)
        case "2":
            print(lista_frasi)
            print(lista_giocatori)
        case "3":
            gioco(lista_frasi,lista_giocatori)