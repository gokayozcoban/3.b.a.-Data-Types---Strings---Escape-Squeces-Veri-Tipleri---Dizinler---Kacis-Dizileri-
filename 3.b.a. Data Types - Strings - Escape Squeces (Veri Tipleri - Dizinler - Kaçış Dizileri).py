# Bu durumdan kurtulmanın başka bir yolu da escape squences (kaçış dizileri).
# Kaçış dizilerinden biri de ters slashtır (\).
# One of escape squeneces is backslash.
print('Türkiye\'nin başkenti Ankara\'dır.')
Türkiye'nin başkenti Ankara'dır.
# Ters slash (\)'ın burada yaptığı, görmesini istemediğimiz karakteri kod içer-
# risinde Python'dan gizlemek. "Burada tek tırnak var ama sen bunu string oluş-
# turan bir unsur olarak görme!" demek istedik ters slash kullanarak.

# Aynı şekilde escape squences'ın bir diğeri de üç tırnağın yaptığı gibi satır-
# ları altalta sıralamaktır. Yukarıda yazdığım şu kodu...:
print("""Bu, stringlerde üç tırnak
kullanımına
bir örnektir.""")
Bu, stringlerde üç tırnak
kullanımına
bir örnektir.

# ... böyle yazarak bu şekilde çıktı alabilirken, şu şekilde escape squence kul-
# lanarak da yazabiliriz:
print("Bu, stringlerde üç tırnak \nkullanımına \nbir örnektir.")
Bu, stringlerde üç tırnak 
kullanımına 
bir örnektir.
# HATIRLATMA: \n escape squence'ı, alt satıra geçerek yazılması istenilen keli-
# menin başına yapışık olarak kullanılırsa çıktı yukarıdaki gibi düzenli görü-
# nür. Aksi taktirde kullanımında şöyle bir düzensiz çıktı verecektir:
print("Bu, stringlerde üç tırnak\n kullanımına\n bir örnektir.")
Bu, stringlerde üç tırnak
 kullanımına
 bir örnektir.
# \n escape squence'ı tüm kelimelere de birleştirilerek de düzgün verir:
print("Bu, stringlerde üç tırnak\nkullanımına\nbir örnektir.")
Bu, stringlerde üç tırnak 
kullanımına 
bir örnektir.
# Ama bu seferde okunaklı, anlaşılabilir bir kod yazamamış oluruz.

# Bir diğer escape squence'ı is \t'dir. \t, cümle içinde istenilen yere bir tab
# uzunluğunda boşluk koyar:
print("Bir tab \tboşluk konmasını istediğim yer: \tburası.")
Bir tab 	boşluk konmasını istediğim yer: 	burası.
# \t'yi de kullanırken \t'yi yukarıdaki gibi boşluğun gelmesini istediğimiz yer-
# den sonra başlayan kelimeye bitişik yazarsak çıktıyı daha düzgün alabiliriz.
# Bu özellik boşlukları doldurmaca gibi içerik hazırlanırken kullanılabilir:
print("Gökay Özçoban isninin baş harfleri \tve \t'dür.")
