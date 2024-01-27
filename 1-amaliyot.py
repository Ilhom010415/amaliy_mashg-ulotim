# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:23:31 2024

@author: Rahmonov_Ilhom
"""
#           # JUFT SONGA TEKSHIRISH
# juft_son = int(input("Juft son kiriting: \n >>> "))
# if juft_son%2 == 0:  # Agar kiritgan soningizni qoldig`i 0 ga teng bo`lsa
#     print("Rahmat! 👌") # demak u juft
# else:
#     print("Siz toq son kirittingiz😒") # 0 ga teng bo`lmasa tog`

#           #FOYDALANUVCHIDAN YOSHINI SO`RASH va CHIPTA BERISH
# yosh = int(input("Yoshingiz nechida? \n >>> "))
# if 7>=yosh or yosh>=65:
#     narh = 0
# elif yosh<18:
#     narh = 10000
# elif yosh>18:
#     narh = 20000
# print(f"Sizga kirish narhi {narh} so\'m ")

#         # ikkita sonni taqqoslash, foydalanuvchi kiritsin
# print("Keling sonlarni taqqoslaymiz! >>>")
# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# if x>y:
#     print(f"{x} soni {y} sonidan katta")
# elif x<y:
#     print(f"{y} soni {x} sonidan katta")
# else:
#     print("Bu sonlar teng...")
    
#         # Do`kondagi kerakli maxsolot borligini tekshirish
# maxsulotlar = ["olma", "o`rik", "un", "non", "suv", "kartoshka", "pamidor", "piyoz", "sut", "muzqaymoq", "go`sht", "shakar", "choy", "go`yo", "tuz", "non", "qatiq", "makaron", "yog`", "kofe"]

# # Bo'sh savat ro'yxati
# savat = []

# # Foydalanuvchidan savatga kamida 5 ta mahsulot kiritishini so'raymiz
# print("5 ta maxsulot kiriting: ")
# for n in range(5):
#     mahsulot = input(f"{n + 1}-mahsulotni kiriting: ")
#     savat.append(mahsulot.lower())  # Kichik harflarga aylantirish

# # Savatdagi mahsulotlarni mahsulotlar ro'yxati bilan solishtiramiz
# for mahsulot in savat:
#     if mahsulot in maxsulotlar:
#         print(f"{mahsulot.capitalize()} do`konimizda bor.")
#     else:
#         print(f"{mahsulot.capitalize()} do`konimizda yo`q.")

        # 2-qisim

# maxsulotlar = ["olma", "o`rik", "un", "non", "suv", "kartoshka", "pamidor", "piyoz", "sut", "muzqaymoq", "go`sht", "shakar", "choy", "go`yo", "tuz", "non", "qatiq", "makaron", "yog`", "kofe"]

# # Bo'sh savat ro'yxati
# savat = []

# # Foydalanuvchidan savatga kamida 5 ta mahsulot kiritishini so'raymiz
# print("5 ta maxsulot kiriting: ")
# for n in range(5):
#     mahsulot = input(f"{n + 1}-mahsulotni kiriting: ")
#     savat.append(mahsulot.lower())  # Kichik harflarga aylantirish
    
# # Yangi ro`yxat mavjud va do`konda yo`q bolgan mahsulotlar
# bor_mahsulotlar = []
# yoq_mahsulotlar = []

# # Savatdagi mahsulotlarni mahsulotlar ro'yxati bilan solishtiramiz
# for mahsulot in savat: 
#     # bor maxsulotlarni yangi ro`yxatga ko`chiramiz
#     if mahsulot in maxsulotlar:
#         bor_mahsulotlar.append(mahsulot.lower())  # Kichik harflarga aylantirish
#     # agar yo`q bo`lsa yo`q maxsulotlar ro`yxatini beramiz        
#     else:
#         yoq_mahsulotlar.append(mahsulot.lower())  # Kichik harflarga aylantirish

# # bu yerda do`konda bor maxsulotlarni bor yoki yo`qligini tekshirib 
# # agar yo`q bolsa yo`q maxsulotlar ro`yxatini beramiz        
# if len(yoq_mahsulotlar) > 0:
#     print(f"Siz so`ragan:\n{bor_mahsulotlar}\nBizda bor.")
#     print(f"Ammo siz so`ragan:\n{yoq_mahsulotlar}\nBizda yo`q")
# else:
#     print("Siz so`ragan mahsulotlarning barchasi bor.")

#           # LOGIN YARATISH VA KIRISH
# mavjud_log = ['Rahmonov', 'Ilhom', 'Mexmonov', 'Hushnud', 'Sharopov','Shamsiddin']
# # Bo`sh ro`yxat yaratamiz
# yangi_log = []

# # login kiritishlarini so`raymiz
# log1 = str(input("Ismingizni kiriting: "))
# yangi_log.append(log1.lower())  # Kichik harflarga aylantirish va ro`yxatga qo`shish

# log2 = str(input("Familyangizni kiriting: "))
# yangi_log.append(log2.lower())  # Kichik harflarga aylantirish va ro`yxatga qo`shish

# #kiritilgan ro`yxatni mavjud ro`yxat bilan solishtiramiz
# for log1 in yangi_log:    # yangi loglarning ichidagilardan biri bo`lsa
#     if log1 in mavjud_log:
#         print("Bu login band, iltimos qayta kiriting: ")

        

