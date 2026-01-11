def portfoy(r):
    print("onerilen dagilim:")
    if r == "dusuk":
        print("altin %50")
        print("faiz %50")
    elif r == "orta":
        print("kiymetli maden %40")
        print("hisse %30")
        print("faiz %30")
    elif r == "yuksek":
        print("hisse %40")
        print("kripto %10")
        print("etf %30")
        print("kiymetli maden %20")

while True:
    print("\nyatirim tavsiye programi")
    print("cikmak icin q yaz")

    para = input("kac tl yatirim yapacaksin?: ")

    if para == "q":
        print("program kapandi")
        break

    if para.isdigit() == False:
        print("sayi girmen lazim")
        continue

    para = int(para)

    if para < 100000:
        print("risk: yuksek")
    elif para <= 1000000:
        print("risk: orta")
    else:
        print("risk: dusuk")

    r = input("ne kadar riske girersin? (dusuk/orta/yuksek): ")

    if r == "dusuk" or r == "orta" or r == "yuksek":
        portfoy(r)
    else:
        print("yanlis girdin")