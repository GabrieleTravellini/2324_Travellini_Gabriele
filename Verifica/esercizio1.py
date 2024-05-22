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

def stampamenu():
    print("1) aggiungere un nuovo oggetto alla lista")
    print("2) eliminare uno specifico oggetto dalla lista")
    print("3) visualizzare l'elenco degli oggetti presenti nella lista")
    print("4) salvare l'elenco su file")
    print("5) caricare dal file un elenco già fatto")
    print("6) esci dal programma")

def aggiungi(lista):
    errore = True
    while errore:
        a = input("Aggiungi quello che vuoi: ")
        if a == " ":
            errore = True
            print("non puoi inserire cose vuote")
        else:
            lista.append(a)
            errore = False


def elimina(lista):
    for i in lista:
        print(i)
    print("Quale oggetto vuoi eliminare?")
    errore = True
    while errore:
        coso = input("Inserisci l'oggetto da eliminare: ")
        errore = False
        if coso not in lista:
            errore = True
            print("L'oggetto non è presente nella lista")
        else:
            lista.remove(coso)
            errore = False

def visualizza(lista):
    for i in range(len(lista)):
        print(f"Elemento {i}: {lista[i]}")

def salva(lista):
    nome = input("Inserisci un nome")
    file = open(nome+".myl","a")
    for i in lista:
        file.write(i +"\n")
    file.close()

def carica(lista):
    try:
        file = input("Inserisci il nome del file: ")
        f = open(file,"r")
        for i in f:
            lista.append(i)
    except:
        print("Il file non esiste")


lista = []

s = ""
while s != "6":
    stampamenu()
    a = input("Fai la tua scelta: ")
    s = scelta(a)
    match s:
        case "1":
            aggiungi(lista)
        case "2":
            elimina(lista)
        case "3":
            visualizza(lista)
        case "4":
            salva(lista)
        case "5":
            carica(lista)
        case "6":
            quit()
