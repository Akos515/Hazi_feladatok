#10 és 20 közötti számok kiiratása
list = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]
for i in list:
    if i >= 10 and 20 >= i:
        print(i, end=" ")
print()

#10-nél kisebb, 20-nál nagyobb
for i in list:
    if i > 20 or 10 > i:
        print(i, end=" ")
print()

#3 szám bekérése, majd legkisebb legnagyobb kiiratása

# szam1 = int(input("Kérek egy számot"))
# szam2 = int(input("Kérek egy számot"))
# szam3 = int(input("Kérek egy számot"))
# if szam1 > szam2 and szam1 > szam3:
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
print()

# x = int(input("A dolgozat pontszáma:"))
# if x < 50:
#     print("az érdemjegy: 1")
# elif 50 < x and x <60:
#     print("az érdemjegy: 2")
# elif 60 < x and x <70:
#     print("az érdemjegy: 3")
# elif 70 < x and x <85:
#     print("az érdemjegy: 4")
# elif 85 < x:
#     print("az érdemjegy: 5")
print()

# szam = int(input("Adjon meg egy számot: "))
# if szam % 5 == 0 or szam % 3 == 0:
#     print("A szám osztható 3-mal vagy 5-tel")
# else:
#     print("A szám NEM osztható 3-mal vagy 5-tel")
print()

# osszeg = int(input("Kérek egy maximumot"))
# for i in range(10):
#     int(input("Kérek egy számot"))
#     if osszeg > int(input("Kérek egy számot")):
#         osszeg = osszeg - int(input("Kérek egy számot"))
#     else:
#         break
# print("hiba")
print()

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

