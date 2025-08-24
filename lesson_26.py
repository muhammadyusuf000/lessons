def avto_info(kampaniya, madel, rangi, karobka, yili, narhi=25000):
    avto = {'kampaniya':kampaniya,
            'madel':madel,
            'rangi':rangi,
            'karobka':karobka,
            'yili':yili,
            'narhi':25000}
#     return avto

# print("saytimizdagi avtolar ro'yhatini shakillantiramiz")
# avtolar = []
# while True:
    print("\nQuyidagi ma'lumotlarni kiriting\n", end="")
    kampaniya=input("Ishlab chaqiruvchi:")
#     madel=input("Madeli: ")
#     rangi=input("Rangi: ")
#     karobka=input("Karobka turi: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("25000: ")
    
#     avtolar.append(avto_info(kampaniya, madel, rangi, karobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no):")
#     if javob.lower() != 'yes':
#         break
    
# print("\nRo'yxatdagi avtomabillar:")    
# for a in avtolar:
#     print(f"{a['yil']} {a['kampaniya']} {a['madel']}, Rangi: {a['rang']}, Karobka:{a['karobkasi']}, narh:{a['narh']}")

#2-dars

def user_info(ismi, familyasi, t_yil, t_joy, eamil=None, telefon=None):
    user = {'ismi':ismi,
            'familyasi':familyasi,
            't_yil':t_yil,
            't_joy':t_joy,
            'email':email,
            'telefon':telefon}
    return user

print("Foydalanuvchi ro'yhatini shakellentiramiz.")
users = []

while True:
    print("\nQuyidagi ma'lumotlarni kiriting\n", end="")
    ismi=input("Foydalanuvchi ismi: ")
    familyasi=input("Foydalanuvchining familyasi: ")
    t_yil=input("Tug'ilgan yili: ")
    t_joy=input("Tug'ilgan joyi: ")
    email=input("Foydalanuvchi emaili: ")
    telefon=input("Foydalanuvchi telefon raqami: ")
    
    users.append(user_info(ismi, familyasi, t_yil, t_joy, email, telefon))
    javob = input("Yana foydalanuvchi qo'shasizmi? (yes/no):")
    if javob.lower() != 'yes':
        break

print("\nRo'yhatdagi Faydalanuvchilar:")
for a in users:
    print(f"foydalanuvchi ismi {a['ismi']}\nFoydalanuvchi familyasi {a['familyasi']}\nFoydalanuvchi t_yil {a['t_yil']}\nFoydalanuvchi t_joy {a['t_joy']}\nFoydalanuvchi email {a['email']}\nFoydalanuvchi telefon {a['telefon']}")

    