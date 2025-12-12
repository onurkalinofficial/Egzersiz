
print("---HARF NOTU HESAPLAMA ARACINA HOŞ GELDİNİZ---")

sınav1 = float(input("vize sınavı notunuzu giriniz: "))
sınav2 = float(input("final sınavı notunuzu giriniz: "))

vize = sınav1 * 40/100
final = sınav2 * 60/100

ort = vize + final

if ort >=90 :
    print("tebrikler harf notunuz AA")

elif ort>=80 :
    print("harf notunuz BA")

elif ort>=70 :
    print("harf notunuz BB")

elif ort>=60 :
    print("harf notunuz CC")

elif ort>=50 :
    print("harf notunuz CD")

elif ort>=40 :
    print("harf notunuz DC")

elif ort>=30 :
    print("harf notunuz DD")

elif ort>=20 :
    print("harf notunuz FD, kaldınız.")

else:
    print("harf notunuz FF, kaldınız.")

print("Başarılar, iyi günler.")



