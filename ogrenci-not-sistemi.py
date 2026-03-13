
not_listesi=[]
basarili=[]
basarisiz=[]


while True:
      try:
       ders_notu= int(input("Lütfen sınav sonucuzu giriniz"))
      except:
       print("Lütfen sayı giriniz")
      
      if ders_notu>=0 and ders_notu<=100:
          
       not_listesi.append(ders_notu)
       
      else: 
          print("HATALI NOT GİRİŞİ TEKRAR DENEYİNİZ")
      sayac=len(not_listesi)
      if sayac==10 :
          break
      
print("Öğrenci Notları: ",not_listesi)

for i in not_listesi:
      if i>=50 :
          basarili.append(i)
          
      else :
         basarisiz.append(i)
         
ortalama = sum(not_listesi) / len(not_listesi)

print("\nSınıf Ortalaması:", ortalama)
print("En yüksek not:", max(not_listesi))
print("En düşük not:", min(not_listesi))


print("Başarılı Öğrenci Notu",basarili)
print("Başarısız Öğrenci Notu",basarisiz)

basarili_ogr_sayisi=print("Başarılı Öğrenci Sayısı",len(basarili))
basarisiz_ogr_sayisi=print("Başarısız Öğrenci Sayısı", len(basarisiz))





















