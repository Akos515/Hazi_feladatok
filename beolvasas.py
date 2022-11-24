with open("olvasandok/kerites.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        oldal = sor[0]
        szelesseg = sor[1]
        szin = sor[2]

hosszusag = []
with open("olvasandok/fogado.txt", encoding="utf8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        vnev = sor[0]
        knev = sor[1]
        idopont = sor[2]
        foglalasidopontja = sor[3]
        hosszusag.append(adat)
print(len(hosszusag))