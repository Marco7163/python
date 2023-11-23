def media_gol_partite(tupla_partite):
    somma=0
    cont=0
    for casa,opsite,pcasa,pospite in tupla_partite:
        somma+=pcasa
        somma+=pospite
        cont+=1
    media = somma/cont
    return media   

tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

mediaGolPartite = media_gol_partite(tupla_partite)
print(media_gol_partite)