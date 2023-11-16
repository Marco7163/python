def analizza(nome):
    
    somma=0
    cont=0

    for mese, *valore in dati:
        cont+=1
        if type(valore) == int:   
            somma += valore
            
    media = somma/cont

    for mese, *valore in dati:
        valoreMax=0
        valoreMin=1000

        if valore>valoreMax:
            valoreMax = valore
            meseMax = mese

        if valore<valoreMin:
            valoreMin = valore
            meseMin = mese    
    
    tupla[0] = media
    tupla[1][0] = valoreMax
    tupla[1][1] = meseMax
    tupla[2][0] = valoreMin
    tupla[2][1] = meseMax

    return tupla

tupla = []

datiPluviometrici = {
    ("Milano", (("Gennaio", 20),("Febbraio", 0), ("Marzo", 28),("Aprile", 15), ("Maggio", 5),("Giugno", 8))),
    ("Roma", (("Gennaio", 18),("Febbraio", 25), ("Marzo", 18),("Aprile", 25), ("Maggio", 0),("Giugno", 5))),
    ("Napoli", (("Gennaio", 15),("Febbraio", 3), ("Marzo", 7),("Aprile", 11), ("Maggio", 25),("Giugno", 28)))
}

for nome, *dati in datiPluviometrici:
    print(f"{nome}\n")
    tupla = analizza(nome)
    print(tupla)