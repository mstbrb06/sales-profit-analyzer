print("SALES & PROFIT ANALYZER PROGRAM")

while True:
    try:
        urun_sayisi = int(input("Lütfen ürün sayısını giriniz: "))
        if urun_sayisi <= 0:
             print("Ürün sayısı 0'dan büyük olmalıdır.")
        else:
             break
    except:
        print("Geçerli bir sayı giriniz.")


            
toplam_kar = 0
toplam_ciro = 0
en_yuksek_kar = None
en_karli_urun = ""

for i in range(urun_sayisi):

    print("\n---", i + 1, ". Ürün ---")

    while True:
       urun = input("Ürün adı: ")
       if urun.isdigit() or urun == "":
           print("Ürün adı sayı olamaz veya boş bırakılamaz. Lütfen geçerli bir ürün adı giriniz.")  
       else:
           break
    
    while True:
        try:
            adet = int(input("Adet: "))
            if adet <= 0:
                print("Adet 0'dan büyük olmalıdır.")
            else:
                break
        except:
            print("Geçerli bir sayı giriniz.")

    while True:
        try:
            birim_fiyat = float(input("Birim fiyat: "))
            if birim_fiyat <= 0:
                print("Birim fiyat 0'dan büyük olmalıdır.")
            else:
             break
        except:
            print("Geçerli bir sayı giriniz.")

    while True:
        try:
            birim_maliyet = float(input("Birim maliyet: "))
            if birim_maliyet <= 0:
                print("Birim maliyet 0'dan büyük olmalıdır.")
            else:
                break
        except:
            print("Geçerli bir sayı giriniz.")

    ciro = adet * birim_fiyat
    maliyet = adet * birim_maliyet
    kar = ciro - maliyet
    kar_orani = (kar / ciro) * 100
    print("Kâr Oranı:", round(kar_orani, 2), "%")

    toplam_kar += kar
    toplam_ciro += ciro

    if kar > 0:
        print("Kar:", kar)
    elif kar < 0:
        print("Zarar:", kar)
    else:
        print("Ne kar ne de zarar")

    if en_yuksek_kar is None or kar > en_yuksek_kar:
     en_yuksek_kar = kar
    en_karli_urun = urun
    
genel_kar_orani = (toplam_kar / toplam_ciro)* 100
print("\n--- Satış Raporu ---")
print("Toplam Ciro:", round(toplam_ciro, 2))
print("Toplam Kar:", round(toplam_kar, 2))
print("En Karlı Ürün:", en_karli_urun)
print("En Yüksek Kar:", round(en_yuksek_kar, 2))
print("Genel Kar Oranı:", round(genel_kar_orani, 2), "%")
input("\nProgramı kapatmak için Enter'a basın...")
