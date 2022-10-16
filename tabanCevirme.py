print("""
                *************
                *HOSGELDINIZ*
                *************""")
i = 0
while i != 3:
    print("----------------------------------------------------------")
    print("1- İkilik tabandan onluk tabana cevirme")
    print("2- Onluk tabadan ikilik tabana cevirme")
    print("3 - Cikis")
    i = int(input(">Yapmak istediginiz islemi tuslayiniz-> "))
    if i == 1:
        j = 1
        sonuc = 0
        uzunluk = 0
        olmayacak="23456789"
        while j != 0:
            sayi = input("Ikilik tabandan onluk tabana cevirmek istediginiz sayiyi giriniz\n"
                         "(Gireceginiz sayi yalnizca 1 ve 0 icermelidir)-> ")
            for _ in sayi:
                uzunluk = uzunluk + 1
            if sayi == "1" or "0":
                if _ not in olmayacak:
                    for i in sayi:
                        uzunluk = uzunluk - 1
                        carpim = int(i) * 2 ** uzunluk
                        sonuc = sonuc + carpim
                    print("Sayinizin onluk tabandaki karsiligi : ", sonuc)
                    j = 0
                else:
                    print("\nHatali karakter girdiniz! Lutfen gecerli rakamlarla tekrar; ")
            else:
                print("\nHatali karakter girdiniz! Lutfen gecerli rakamlarla tekrar; ")

    elif i == 2:
        sayi = int(input("Onluk tabandan ikilik tabana cevirmek istediginiz sayiyi giriniz-> "))
        sonuc = ""
        while sayi > 1:
            kalan = sayi % 2
            sayi = sayi // 2
            sonuc = str(kalan) + sonuc
        if sayi > 0:
            sonuc = str(sayi) + sonuc
            print("Sayinizin ikilik tabandaki karsiligi: ", sonuc)
        else:
            print("Pozitif bir sayi gerek!")

    elif i == 3:
        print("Basarili bir sekilde cikis yaptiniz. Hoscakalin :)")
    else:
        print("Hatali tuslama yaptiniz, lutfen seciminizi tekrar yapiniz!")
