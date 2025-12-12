print("---BKI HESAPLAMA ARACINA HOŞ GELDİNİZ---")

boy = float(input("boyunuzu giriniz: "))
kilo = float(input("kilonuzu giriniz: "))

bki = kilo/boy**2
print("bki: ", format (bki, ".2f"))

if bki<=18.49 :
    print("zayıfsınız.")

elif bki<=24.90 :
    print("normal kilodasınız.")

elif bki<=29.90 :
    print("fazla kilolusunuz.")

elif bki<=39.90 :
     print("obezsiniz.")

elif bki>=39.91 :
     print("morbid obezsiniz")

print("---SAĞLIKLI GÜNLER DİLERİZ---")


