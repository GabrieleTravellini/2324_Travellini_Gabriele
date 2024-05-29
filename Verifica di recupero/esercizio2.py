import requests

def menu():
    print("1) Genera battuta casuale")
    print("2) Genera battuta scelta da te")
    print("0) Esci")

def categoria():
    categorie = {"Generale":"general","Toc-Toc!":"knock-knock","Programmazione":"programming","Papà":"dad"}
    print(categorie)
    errore = True
    while errore:
        robo = input("Inserisci il tipo di battuta da generare: ")
        if robo not in categorie:
            errore = True
            print("Seleziona una categoria presente")
        else:
            errore = False
            risp = requests.get(f"https://official-joke-api.appspot.com/jokes/{categorie[robo]}/random")
            json = risp.json()
            print(json[0]["setup"],json[0]["punchline"])

def casuale():
    risposta = requests.get(f"https://official-joke-api.appspot.com/jokes/random")
    json = risposta.json()
    print(json["setup"],json["punchline"])

def scelta():
    scelte = ("0","1","2")
    errore = True
    while errore:
        errore = False
        scelta = input("Fai la tua scelta: ")
        if scelta not in scelte:
            errore = True
            print("Scelta non accettabile")
        else:
            errore = False
            return scelta

s = ""
while s != "0":
    menu()
    s = scelta()
    match s:
        case "1":
            casuale()
        case "2":
            categoria()
        case "3":
            quit()