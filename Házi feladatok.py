#10 és 20 közötti számok kiiratása
#

#3 szám bekérése, majd legkisebb legnagyobb kiiratása

# szam1 = int(input("Kérek egy számot"))
# szam2 = int(input("Kérek egy számot"))
# szam3 = int(input("Kérek egy számot"))
# if szam1 > szam2 and szam1 > szam3:list = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]
# # for i in list:
# #     if i >= 10 and 20 >= i:
# #         print(i, end=" ")
# # print()
# #
# # #10-nél kisebb, 20-nál nagyobb
# # for i in list:
# #     if i > 20 or 10 > i:
# #         print(i, end=" ")
# # print()
#     print(f"a legnagyobb szám a {szam1}")
# elif szam2 > szam1 and szam2 > szam3:
#     print(f"a legnagyobb szám a {szam2}")
# elif szam3 > szam1 and szam3 > szam2:
#     print(f"a legnagyobb szám a {szam3}")
#
# if szam1 < szam2 and szam1 < szam3:
#     print(f"a legkisebb szám a {szam1}")
# elif szam2 < szam1 and szam2 < szam3:
#     print(f"a legkisebb szám a {szam2}")
# elif szam3 < szam1 and szam3 < szam2:
#     print(f"a legkisebb szám a {szam3}")
# print()

# x = int(input("A dolgozat pontszáma:"))
# if x < 50:
#     print("az érdemjegy: 1")
# elif 50 < x and x <60:
#     print("az érdemjegy: 2")
# elif 60 < x and x <70:
#     print("az érdemjegy: 3")
# elif 70 < x and x <85:
#     print("az érdemjegy: 4")
# elif 85 <= x:
#     print("az érdemjegy: 5")
# print()

# szam = int(input("Adjon meg egy számot: "))
# if szam % 5 == 0 or szam % 3 == 0:
#     print("A szám osztható 3-mal vagy 5-tel")
# else:
#     print("A szám NEM osztható 3-mal vagy 5-tel")
# print()

# osszeg = int(input("Kérek egy maximumot"))
# for i in range(10):
#     int(input("Kérek egy számot"))
#     if osszeg > int(input("Kérek egy számot")):
#         osszeg = osszeg - int(input("Kérek egy számot"))
#     else:
#         break
# print("hiba")
# print()

# x = int(input("írj be egy egész számot:"))
# y = int(input("írj be egy egész számot:"))
# z = int(input("írj be egy egész számot:"))
# if x + y == z:
#     print(f"{z} egyenlő {x} + {y} összegével")
# elif x + z == y:
#     print(f"{y} egyenlő {x} + {z} összegével")
# elif y + z == x:
#     print(f"{x} egyenlő {z} + {y} összegével")
# else:
#     print("2 szám összege nem adja meg a 3. szám értékét")
# print()

# x = int(input("írj be egy egész számot:"))
# y = int(input("írj be egy egész számot:"))
# z = int(input("írj be egy egész számot:"))
# if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
#     print("a számok párosak")
# else:
#     print("a számok nem párosak")
# print()

# szam1 = int(input("írj be egy egész számot:"))
# szam2 = int(input("írj be egy egész számot:"))
# for i in range(szam1,szam2,1):
#     if i % 2 == 0:
#         print(i)
# print()

# Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna)
# jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
# - egyikük sem jön kosarazni,
# - mind a ketten jönnek kosarazni,
# - csak az egyikük jön kosarazni.

# henrik = (input("Jön Henrik ma kosarazni?: "))
# hanna = (input("Jön Hanna ma kosarazni?: "))
# if henrik == "igen" and hanna == "igen":
#     print("mind a ketten jönnek kosarazni.")
# elif henrik == "igen" and hanna == "nem" or henrik == "nem" and hanna == "igen":
#     print("csak az egyikük jön kosarazni.")
# else:
#     print("egyikük sem jön kosarazni.")
# print()

# Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
# - csak 3-mal osztható,
# - csak 4-gyel osztható,
# - 3-mal és 4-gyel is osztható,
# - sem 3-mal, sem 4-gyel nem osztható!

# valasz = int(input("Kérek egy számot: "))
# if valasz % 3 == 0 and valasz % 4 == 0:
#     print("3-mal és 4-gyel is osztható")
# elif valasz % 3 == 0 and not valasz % 4 == 0:
#     print("csak 3-mal osztható")
# elif valasz % 4 == 0 and not valasz % 3 == 0:
#     print("csak 4-gyel osztható")
# else:
#     print("sem 3-mal, sem 4-gyel nem osztható!")
# import math
# #
# sugar = int(input("Kérem a kör sugarát: "))
# kerulet = sugar * 2 * math.pi
# print(f"kerület: {round(kerulet)}")

#A megadott szó: befogadóképességű
#a felhasználótól kérjünk be egy karaktert és ellenőrizzük hogy megtalálható-e vagy sem a befogadóképességű szóban?
#ha szerepel benne akkor hányadik karakter az?

# hely = 0
# szo = "befogadóképességű"
# valasz = input("Kérek egy betűt: ")
# if valasz in szo:
#     print("Találat!")
#     for i in szo:
#         if valasz in i:
#             print(f"A betű a {hely + 1} helyen található")
#         hely += 1
# else:
#     print("Nem található!")

# import random
# szamoklista = [random.randrange(0,101,1) for elem in range(50)]
#
# for elem in szamoklista:
#     if elem % 2 == 0:
#         for i in elem:
#             print(f"Páros számok: {i}")

tanuloszam = 0
jegyek = []
print("írja be a tanulók érdemjegyét")
while True:
    tanuloszam += 1
    adat = int(input(f"{tanuloszam}. tanuló:"))
    jegyek.append(adat)
    if adat == 0:
        break
a = (len(jegyek)-1)
print(jegyek)
print(f"ennyi jegyet kaptak a tanulók {a}")
print(f" {jegyek.count(5)} tanuló kapott 5öst\n {jegyek.count(4)} tanuló kapott 4est\n {jegyek.count(3)} tanuló kapott 3mast\n {jegyek.count(2)} tanuló kapott 2est\n {jegyek.count(1)} tanuló kapott 1est\n")
atlag = sum(jegyek) / a
print(f"Az átlag {atlag}")