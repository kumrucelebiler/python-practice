import time
def kullanici_adini_al():
    isim = input("İsminizi giriniz: ")
    return isim


def kahve_turunu_sec():
    print("\n------ KAHVE MENÜSÜ ------")
    print("1 - Türk Kahvesi (35 TL)")
    print("2 - Latte (55 TL)")
    print("3 - Espresso (45 TL)")
    print("4 - Filtre Kahve (40 TL)")

    try:
        secim = int(input("Seçiminizi yapınız: "))
        return secim
    except:
        print("Lütfen sayı giriniz!")
        return 0


def kahve_turunu_esle(kahve_turu):

    if kahve_turu == 1:
        return "Türk Kahvesi"

    elif kahve_turu == 2:
        return "Latte"

    elif kahve_turu == 3:
        return "Espresso"

    elif kahve_turu == 4:
        return "Filtre Kahve"

    else:
        return None

def seker_tercihini_al():

    secim = input("Şeker ister misiniz? (e/h): ")
    secim = secim.lower()

    if secim == "e":
        return True

    elif secim == "h":
        return False

    else:
        print("Hatalı seçim!")
        return False


def krema_tercihini_al():

    secim = input("Krema ister misiniz? (e/h): ")
    secim = secim.lower()

    if secim == "e":
        return True

    elif secim == "h":
        return False

    else:
        print("Hatalı seçim!")
        return False


def kahve_suresi_hesapla(kahve_turu):

    if kahve_turu == 1:
        return 3.5

    elif kahve_turu == 2:
        return 2.8

    elif kahve_turu == 3:
        return 2.2

    elif kahve_turu == 4:
        return 4.0


def ek_sure_hesapla(seker, krema):

    ek_sure = 0.0

    if seker:
        ek_sure += 0.3

    if krema:
        ek_sure += 0.4

    return ek_sure


def toplam_sure_hesapla(kahve_turu, seker, krema):

    ana_sure = kahve_suresi_hesapla(kahve_turu)
    ekstra = ek_sure_hesapla(seker, krema)

    return ana_sure + ekstra


def kahve_ucreti_hesapla(kahve_turu):

    if kahve_turu == 1:
        return 35

    elif kahve_turu == 2:
        return 55

    elif kahve_turu == 3:
        return 45

    elif kahve_turu == 4:
        return 40


def ek_ucret_hesapla(seker, krema):

    ucret = 0

    if seker:
        ucret += 2

    if krema:
        ucret += 5

    return ucret



def toplam_ucret_hesapla(kahve_turu, seker, krema):
    kahve_ucret = kahve_ucreti_hesapla(kahve_turu)
    ekstra = ek_ucret_hesapla(seker, krema)

    return kahve_ucret + ekstra


def odeme_al(kahve_turu, seker, krema):
    ucret = toplam_ucret_hesapla(kahve_turu, seker, krema)
    odenen = int(input("Ödeme yapınız: "))

    if odenen >= ucret:

        para_ustu = odenen - ucret
        print("Para üstü:", para_ustu)

        return True

    else:

        print("Yetersiz ödeme!")
        print("İşlem iptal edildi.")

        return False


def kahve_hazirla(kahve_turu, seker, krema):

    sure = toplam_sure_hesapla(kahve_turu, seker, krema)

    print("\nKahveniz hazırlanıyor...")
    while sure > 0:
        time.sleep(1)
        sure -= 0.5
        print("Kalan süre:", round(sure,1), "sn")
    print("\nKahveniz hazır! Afiyet olsun ☕")


def kahve_makinesini_baslat():

    isim = kullanici_adini_al()
    print("\nHoşgeldiniz", isim)

    kahve_turu = kahve_turunu_sec()
    kahve = kahve_turunu_esle(kahve_turu)

    if kahve is None:
        print("Hatalı seçim! Program sonlandırıldı.")
        return

    print("\nSeçtiğiniz kahve:", kahve)

    seker = seker_tercihini_al()
    krema = krema_tercihini_al()

    toplam_sure = toplam_sure_hesapla(kahve_turu, seker, krema)
    toplam_ucret = toplam_ucret_hesapla(kahve_turu, seker, krema)

    print("\n------ SİPARİŞ ÖZETİ ------")
    print("Kahve:", kahve)
    print("Şeker:", "Evet" if seker else "Hayır")
    print("Krema:", "Evet" if krema else "Hayır")
    print("Hazırlama süresi:", toplam_sure, "sn")
    print("Toplam ücret:", toplam_ucret, "TL")

    odeme = odeme_al(kahve_turu, seker, krema)

    if odeme:
        kahve_hazirla(kahve_turu, seker, krema)


kahve_makinesini_baslat()