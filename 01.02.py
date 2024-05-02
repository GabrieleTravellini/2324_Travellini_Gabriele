def Perpendicolari(m1,m2):
    
     if m1*m2 == -1:
          return True
     else: 
          return False

print(" y = mx + q")
buonpomeriggio = eval(input("Inserisci il valore di m della prima retta: ")) #eval converte i valori str(1/2) in numeri perciò l'ho utilizzato al posto di float
prof = eval(input("Inserisci il valore di m della seconda retta: "))
print(Perpendicolari(buonpomeriggio,prof))

