import requests

def scelta():

    scelte_possibili = ("EUR","USD","CHF","GBP","AUD","JPY")
    errore = True
    while errore:
        errore = False
        print(scelte_possibili)
        s = input("Inserisci la valuta che vuoi convertire")
        if s not in scelte_possibili:
            print("Inserisci una valuta tra quelle sopra")
            errore = True
        else:
            errore = False
            return s

def cambio():
    s = scelta()
    ciao = int(input("Inserisci un numero da convertire: "))
    b = input("Inserisci l'altra valuta da convertire: ")
    api = requests.get("https://open.er-api.com/v6/latest/USD")
    trasformo = api.json()
    print((trasformo["rates"][s] * ciao))  
    print((trasformo["rates"][b] * ciao))


cambio()
