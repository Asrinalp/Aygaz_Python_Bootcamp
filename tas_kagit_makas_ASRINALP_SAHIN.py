# -*- coding: utf-8 -*-

import random

def tas_kagit_makas_ASRINALP_SAHIN():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Oyunun kuralları:")
    print("1. Taş, Kağıt, Makas oyununu oynayacaksınız.")
    print("2. Öncelikle Oyunu hangi modda oynamak istediğinizi 1 veya 2 seçeneklerini kullanarak belirleyin.")
    print("3. Sonrasında oyun içerisinde sizden seçmenizi istenen seçeneklerden birini seçiniz.")
    print("4. İlk iki turu kazanan oyunun galibi olur.")
    print("5. Beraberlik durumunda iki taraf da sayı kazanamaz.")
    print("6. Klasik seçenekli oyun modunda taş makası yener, makas kağıdı yener, kağıt ise taşı yener.")
    print("7. Futbol seçenekli oyun modunda kimin kimi yendiğini görmek istiyorsan oynayarak öğrenmelisin. :)")
    # Seçenekler
    klasik_secenekler = ["taş", "kağıt", "makas"]
    futbol_secenekler = ["galatasaray", "fenerbahce", "sivasspor", "besiktas", "antalyaspor", "adana demirspor"]


    # Değişkenlerimin isimleri
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0
    oyun_sayisi = 0
    tur_sayisi = 1
    secenekler = []


    print("Hangi oyun modunda oynamak istersiniz?")
    print("1: Klasik Seçenekler (Taş, Kağıt, Makas)")
    print("2: Futbol Seçenekler (Fenerbahçe, Galatasaray, Beşiktaş, vs.)")

    while True:
        try:
            mod = int(input("Lütfen oyuna girmek istediğiniz oyun modu numarasını giriniz (1 veya 2): "))
            if mod == 1:
                secenekler = klasik_secenekler
                print("\nKlasik oyun modunu seçtiniz.")
                break
            elif mod == 2:
                secenekler = futbol_secenekler
                print("\nFutbol oyun modunu seçtiniz.")
                break
            else:
                print("Lütfen geçerli bir mod numarası girin (1 veya 2).")
        except ValueError:
            print("Lütfen geçerli bir mod numarası girin (1 veya 2).")

    # Oyun döngüsü
    while True:
        oyun_sayisi += 1
        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            print(f"\nOyun {oyun_sayisi}: Tur {tur_sayisi}: \n ")
            oyuncu_secimi = input(f"Lütfen seçiminizi yapın ({', '.join(secenekler)}): ").lower()


            if oyuncu_secimi not in secenekler:
                print(f"Geçersiz seçenek! Lütfen {', '.join(secenekler)} seçeneklerinden birini girin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Sonuç bölümünü belirlediğim kodun ana başlangıcı
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik! İki taraf da puan almayacak.")
                print(f"Oyuncu Skoru: {oyuncu_galibiyet}, Bilgisayar Skoru: {bilgisayar_galibiyet}")
                tur_sayisi += 1
                continue
            elif mod == 1:
                # Klasik mod için kazananı belirlediğimiz kısım
                if (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                   (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                   (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                    oyuncu_galibiyet += 1
                    print(f"Turu kazandınız! Oyuncu Skoru: {oyuncu_galibiyet}, Bilgisayar Skoru: {bilgisayar_galibiyet}")
                else:
                    bilgisayar_galibiyet += 1
                    print(f"Bilgisayar turu kazandı! Oyuncu Skoru: {oyuncu_galibiyet}, Bilgisayar Skoru: {bilgisayar_galibiyet}")
            else:
                # Rastgelelik oluşturmak için futbol modunda kazananı belirlediğim algoritma
                oyuncu_index = futbol_secenekler.index(oyuncu_secimi)
                bilgisayar_index = futbol_secenekler.index(bilgisayar_secimi)

                if (oyuncu_index - bilgisayar_index) % len(futbol_secenekler) in [1, 2, 3]:
                    oyuncu_galibiyet += 1
                    print(f"Turu kazandınız! Oyuncu Skoru: {oyuncu_galibiyet}, Bilgisayar Skoru: {bilgisayar_galibiyet}")
                else:
                    bilgisayar_galibiyet += 1
                    print(f"Bilgisayar turu kazandı! Oyuncu Skoru: {oyuncu_galibiyet}, Bilgisayar Skoru: {bilgisayar_galibiyet}")
            tur_sayisi += 1

        if oyuncu_galibiyet == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı.")

        # Oyunun devam edip etmeyeceğini belirlemek için yazdığım kod kısmı
        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"])

        if devam == "evet" and bilgisayar_devam == "evet":
            print("Her iki taraf da oyuna devam etmek istiyor. Yeni oyun başlatılıyor.")
        elif devam == "hayır" and bilgisayar_devam == "evet":
            print("Bilgisayar: Korkup kaçıyor musun? Yine de oyundan çıkmak istiyor musun?")
            tekrar = input("Oyundan çıkmak istediğinize emin misiniz? (evet/hayır): ").lower()
            if tekrar == "evet":
                print("Tamam daha fazla ısrar etmeyeceğim. Tekrar görüşmek üzere!")
                break
            else:
                print("İşte bu hadi bir oyun daha oynayalım.")
                tur_sayisi = 1
                oyuncu_galibiyet = 0
                bilgisayar_galibiyet = 0
                continue
        elif devam == "evet" and bilgisayar_devam == "hayır":
            print("Bilgisayar seninle daha fazla oyun oynamak istemiyor. :(")
            print("Oyun bitti!")
            break
        else:
            print("Bilgisayar: Ben de oynamak istemiyordum zaten.")
            print("Oyunu bitirdiniz. Teşekkürler!")

            break


        # Her oyun sonu sayaçları sıfırlamak için yazdığım bölüm
        tur_sayisi = 1
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0


tas_kagit_makas_ASRINALP_SAHIN()
