# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:50:20 2024

#09-Dars 

 FOR LOOP Operatorlari

@author: Rahmonov Ilhom
"""
#   # Bu siklda biz ro`yxatdagi xar bir elementga aloxida murojat qilamiz
# friends = ["Asadbek", "Navro`zbek", "Soatmurod", "Laziz", "Salohiddin"]
# for friend in friends:
#     print("Assalomu alaykum jigarim", friend) 

# for friend in friends:
#     print(f"Hurmatli do`stim {friend}, sizni 25-may kuni")
#     print("bo`lib o`tadigan bitiruv oqshomiga taklif qilamiz \n")

# sonlar = list(range(1,9))
# for son in sonlar:
#     print(f"{son} nining kvadrati,{son**2} ga teng")

# sonlar_2 = list(range(11))
# sonlar_kvadrati = []
# sonlar_kubi = []
# for son in sonlar_2:
#     sonlar_kvadrati.append(son**2)
#     sonlar_kubi.append(son**3)
# print("Berilgan sonlar: ",sonlar_2)
# print("Kvadrati: ", sonlar_kvadrati)
# print("Kubi: ",sonlar_kubi)

#    # FOR VA INPUT bilan ishlash
# friend = []
# print("5 ta eng yaqin do`stingiz kim?")
# for n in range(5):
#     friend.append(input(f"{n+1}-isimni kiriting: "))
# print(friend)

#  # XAE BIR DO`STIMNING ISMI LISTGA BOSH HARF BILAN YOZILADI

friend = []
print("5 ta eng yaqin do`stingiz kim?")
for n in range(5):
    ism = input(f"{n + 1}-isimni kiriting: ")
    friend.append(ism.title())  # Har bir ismni bosh harf bilan yozib qo'shish
#    friend.append(ism.title().replace("`", "'"))  # Har bir ismni bosh harf bilan yozib qo'shish va o'rniga ` belgisini ' bilan almashtirish
print(friend)





