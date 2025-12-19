print("*****************************")
print("SIRIUS BANKASINA HOŞ GELDİNİZ")
print("*****************************")

print("""
     *İşlemler*

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
4. Çıkış
""")

bakiye = 5000

while True:
    işlem = input("Gerçekleştirmek istediğiniz işlemi giriniz: ")

    if işlem == "4":
        print("İyi günler dileriz.")
        break

    elif işlem == "1":
        print(f"Bakiyeniz {bakiye} TL")

    elif işlem == "2":
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        bakiye += miktar
        print(f"Yeni bakiyeniz {bakiye} TL")

    elif işlem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))

        if bakiye - miktar < 0:
            print("Yetersiz bakiye!")
            print(f"Bakiyeniz {bakiye} TL")
            continue
        else:
            bakiye -= miktar
            print(f"Yeni bakiyeniz {bakiye} TL")

    else:
        print("Geçersiz işlem!")
