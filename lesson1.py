

isim = "Burak"

# Değişkenler: Programlama dillerinde veri saklamak için kullanılan yapılardır.
# Değişkenlerin tanımlanması: değişken_adı = değer
#region Değişkenlerin isimlendirilmesi için kullanılan bazı kurallar:
# 1. Değişken ismi sayı ile başlayamaz.
# örn: 1isim (hatalı)
# 2. Değişken ismi özel karakterler içeremez.
# örn: isim@, isim!, isim# (hatalı)
# 3. Değişken ismi boşluk içeremez.
# örn: isim soyisim (hatalı)
# 4. Değişken ismi tanımlı anahtar kelimeleri içeremez.
# örn: if, else, elif, for, while, break, continue, pass, return, def, class, try, except, finally, raise, import, from, as, in, is, not, and, or, global, nonlocal, lambda, with, yield, del, assert, True, False, None
# 5. Değişken ismi büyük küçük harf duyarlıdır.
# örn: isim, Isim, ISIM, iSiM farklı değişkenlerdir.
# 6. Değişken ismi Türkçe karakter içeremez. (içermemesi best parctice'dır.)
# Best Practise: İlgili yazılım dili (yada framework'ü) ile nasıl daha iyi kod yazılacağı hakkında size fikir veren “bilgiler bütünü”dür.
# 7. Değişken ismi _ (alt çizgi) ile başlayabilir ve bitebilir.
# örn: _isim, isim_, _isim_ (geçerli)
# 8. Değişken ismi sayısal değer içerebilir.
# örn : isim1, isim2, isim3 (geçerli)
# 9. Değişken ismi birden fazla kelime içerebilir.
# İsimlendirme Türleri: camelCase, snake_case, PascalCase, kebab-case
# 10. Değişken ismi tanımlı fonksiyon, sınıf, modül, paket isimlerini içeremez.
# örn: print, input, len, type, range, str, int, float, list, tuple, dict, set, bool, math, os, sys, random, datetime, numpy, pandas, matplotlib, tensorflow, keras
#endregion

print("Merhaba Dünya!") # çkt: Merhaba Dünya!

print("hello world") # çkt: hello world

#region Ekrana Yazdırma
# print(değişken): Değişkenin değerini ekrana yazdırır ve bir alt satıra geçer..
# print("metin"): Metni ekrana yazdırır.
print("metin1") # çkt: metin1
print() # çkt: Boş bir satır ekler.
print("metin2") # çkt: metin2
isim = "Arda"
print(isim) # çkt: Arda



# print(): Boş bir satır ekler.
# print(değişken1, değişken2): Birden fazla değişkeni ekrana yazdırır.
# print("metin" + değişken): Metin ve değişkeni birleştirerek ekrana yazdırır.
# print(4 + 5): İşlem sonucunu ekrana yazdırır.
# print("metin" + 4 + 5): Hata verir. Çünkü metin ve sayı birleştirilemez.
#endregion

#region Değişken Türleri

# String (Metinsel) Değişkenler
# String: Metinsel ifadeleri temsil eder.
# Tanımlama: Tek tırnak ('), çift tırnak ("), üç tırnak (''' veya """) içerisinde tanımlanabilir.
name = "Ali"
print(name) #çkt: Ali
surname = "Yılmaz"
age = "25"

print("Merhaba benim adım " , name , " ve soyadım " , surname , " yaşım ise " , age)
# çkt: Merhaba benim adım Ali ve soyadım Yılmaz yaşım ise 25

# Integer (Tam Sayı) Değişkenler
# Integer: Tam sayıları temsil eder.

num1 = 5
num2 = 10
print(num1 + num2) # çkt: 15
result = num1 + num2
print(result) # çkt: 15

# Float (Ondalıklı Sayı) Değişkenler
# Float: Ondalıklı sayıları temsil eder.
# Tanımlama: Ondalıklı sayılar tam ve ondalık bölüm arasına nokta (.) koyarak ifade edilir.
# Double veri tipi python'da yoktur. Ondalıklı sayılar float veri tipi ile temsil edilir.

num3 = 5.5
num4 = 10.5
print(num3 + num4) # çkt: 16.0 (float)
result = num3 + num4
print(result) # çkt: 16.0 (float)
# %.2f: Ondalıklı sayıları 2 basamak olarak gösterir.
# Noktanın önündeki sayıyı değiştirerek farklı basamak sayıları gösterebilirsiniz.
print("Sonuç: %.2f" % result) # çkt: Sonuç: 16.00

# Boolean (Mantıksal) Değişkenler
# Boolean: Mantıksal verileri temsil eder.
# True: Doğru anlamına gelir. False: Yanlış anlamına gelir.
situation = True
print(situation) # çkt: True
situation = False
print(situation) # çkt: False
#endregion

#region Değişken Tipi Öğrenme
# type(): Değişkenin tipini öğrenmek için kullanılır.

x = 5               # int
y = 3.14            # float
name = "Ali"        # str
is_student = True   # bool




type1 = type(name)
print(type1) # çkt: <class 'str'> (string)
print(type(x)) # çkt: <class 'int'> (integer)
print(type(y)) # çkt: <class 'float'> (float)
print(type(is_student)) # çkt: <class 'bool'> (boolean)
#endregion

#region f-string
# f-string: String ifadeler içerisinde değişkenleri kullanarak ifade etmek için kullanılır.
# Tanımlama: String ifadenin tırnaklarının başına f koyarak ve içerisindeki değişkeni {} içerisine alarak kullanılır.
print(f"Merhaba benim adım {name} ve soyadım {surname} yaşım ise {age}")
# Kaçış Dizileri (Escape Characters) : String ifadeler içerisinde özel karakterleri kullanmak için kullanılır.
# \n: Bir alt satıra geçer.
print("Merhaba\nBenim\nAdım\nAli")
# çkt: Merhaba
#      Benim
#      Adım
#      Ali

# \t: Bir tab (4 space:    ) boşluk bırakır.
print("Merhaba\tBenim\tAdım\tAli")
# çkt: Merhaba    Benim   Adım    Ali
# \": Çift tırnak ekler.
# \': Tek tırnak ekler.
# \\: Ters eğik çizgi ekler.
# Eğer ifademizin kaçış dizilerinden etkilenmesini istemiyorsak başına r koyarak raw string ifadesi oluşturabiliriz.
print(r"Merhaba\nBenim\nAdım\nAli")
# çkt: Merhaba\nBenim\nAdım\nAli
#endregion

#regionDeğişken Tür Dönüşümleri
float_number = 5.5
print(f"float_number değişkeninin ilk tipi {type(float_number)}")
# çkt: float_number değişkeninin ilk tipi <class 'float'>

# int(): Integer türüne dönüştürme işlemi yapar.
float_number = int(float_number)
print(f"float_number değişkeninin ilk dönüşümden sonraki tipi {type(float_number)}")
# çkt: float_number değişkeninin ilk dönüşümden sonraki tipi <class 'int'>

# str(): String türüne dönüştürme işlemi yapar.
float_number = str(float_number)
print(f"float_number değişkeninin ikinci dönüşümden sonraki tipi {type(float_number)}")
# çkt: float_number değişkeninin ikinci dönüşümden sonraki tipi <class 'str'>
# float(), bool(): Float ve Boolean türlerine dönüştürme işlemi yapar.
#endregion

#region Kullanıcıdan Veri Alma
# input(): Kullanıcıdan veri almak için kullanılır.
# input("metin"): Kullanıcıdan veri alırken ekrana metni yazdırır.
# input() fonksiyonu ile alınan veri her zaman string türünde olur.
# input() fonksiyonu ile alınan veriyi diğer türlerde kullanmak için tür dönüşümü yapılmalıdır.
name2 = input("Adınızı giriniz: ")
surname2 = input("Soyadınızı giriniz: ")
age2 = input("Yaşınızı giriniz: ")
print(f"Merhaba benim adım {name2} ve soyadım {surname2} yaşım ise {age2}")
# çkt: Merhaba benim adım Ali ve soyadım Yılmaz yaşım ise 25

#print(f"Merhaba benim adım {name} ve soyadım {surname} yaşım ise {age}, 5 yıl sonra {(age) + 5} yaşında olacağım.") # Hata verir.
# Hatanın nedeni input() fonksiyonu ile alınan verinin (age) string türünde olmasıdır. String bir değişkenle matematiksel işlemler yapılamaz. Bu yüzden tür dönüşümü yapılmalıdır.

print(type(age2)) # çkt: <class 'str'>
age2 = int(age2)
print(type(age2)) # çkt: <class 'int'>
print(f"Merhaba benim adım {name} ve soyadım {surname} yaşım ise {age2}, 5 yıl sonra {age2 + 5} yaşında olacağım.")
# çkt: Merhaba benim adım Ali ve soyadım Yılmaz yaşım ise 25, 5 yıl sonra 30 yaşında olacağım. (veriler kullanıcından alındığı için değişkenlik gösterebilir.)
# input() fonksiyonu için best practice:
number11 = int(input("Bir sayı giriniz: "))
print(type(number11))

isim1 = input("İsminizi Giriniz: ")

#endregion


