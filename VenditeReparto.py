def analizza_consumi_energetici(citta,risorsa):
    somma = 0
    cont = 0
    max = 0    
    tupla = []
    for citta ,* dati in tupla_consumi_energetici:
        for mese ,* dati2 in dati:
            for risorsa ,* consumo in dati2:
                somma += consumo
                cont+=1

                if(consumo>max):
                    max_risorsa=consumo
                    meseMax_risorsa = mese
                
    media_risorsa = somma/cont           

    tupla[0] = media_risorsa
    tupla[1][0] = max_risorsa
    tupla[1][1] = meseMax_risorsa

    return tupla

tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 80)),
        ("marzo", ("gas", 220)),
        ("aprile", ("elettrico", 180)),
        ("aprile", ("gas", 90)),
    ]
    ),

    ("Brescia", [
        ("gennaio", ("elettrico", 150)),
        ("gennaio", ("gas", 80)),
        ("febbraio", ("elettrico", 240)),
        ("febbraio", ("gas", 250)),
        ("marzo", ("elettrico", 180)),
        ("marzo", ("gas", 230)),
        ("aprile", ("elettrico", 300)),
        ("aprile", ("gas", 210))
    ]
    ),

    ("Roma", [
        ("gennaio", ("elettrico", 120)),
        ("gennaio", ("gas", 210)),
        ("febbraio", ("elettrico", 160)),
        ("febbraio", ("gas", 240)),
        ("marzo", ("elettrico", 160)),
        ("marzo", ("gas", 120)),
        ("aprile", ("elettrico", 240)),
        ("aprile", ("gas", 180))
    ]
    )
)

risultato_analisi = []

for citta ,* dati in tupla_consumi_energetici:
    for mese ,* dati2 in dati:
        for risorsa ,* consumo in dati2:
            x = 0
        
risultato_analisi = analizza_consumi_energetici(citta,risorsa)
print(risultato_analisi)

