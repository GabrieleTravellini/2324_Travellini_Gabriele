lista = []

def carica(lista):
    s = open("gusti1.txt","r")
    for i in s:
        lista.append(i.strip())
carica(lista)
print(lista)