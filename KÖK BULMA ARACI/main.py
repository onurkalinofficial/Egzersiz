print("---KÖK BULMA ARACINA HOŞ GELDİNİZ---")

a = int(input("a sayısını gir: "))
b = int(input("b sayısını gir: "))
c = int(input("c sayısını gir: "))
delta = b**2 - 4*a*c
kök1 = -b-delta**0.5/(2*a)
kök2 = -b+delta**0.5/(2*a)

print("kök1: {}\nkök2: {}".format([kök1],[kök2]))


