def prenotazioni_cliente(prenotazioni,cliente):
    arr = []
    for nome,data,persone,tavolo in prenotazioni:
        if nome==cliente:
            x= data,persone,tavolo
    arr.append(x)
    return arr

def conto_totale(prenotazioni, data):
    c=0
    for nome,giorno,persone,tavolo in prenotazioni:
        if giorno==data:
            c+=1
    return c

prenotazioni = []

aggiungi_prenotazione(prenotazioni, "Maria", "04-10-2023", 4, 3)
aggiungi_prenotazione(prenotazioni, "Pietro", "04-10-2023", 2, 2)
aggiungi_prenotazione(prenotazioni, "Carlo", "04-10-2023", 5, 5)

print(prenotazioni)
print("Tavoli disponibili per il 04-10-2023:", tavoli_disponibili(prenotazioni, "04-10-2023"))
print("Prenotazioni di Maria:", prenotazioni_cliente(prenotazioni, "Maria"))
print("Conto totale per il 04-10-2023:", conto_totale(prenotazioni, "04-10-2023"))