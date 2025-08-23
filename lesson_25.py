# # # def kvadrat_fuksiya():
# # #     son = int(input("Istalgan sonni kiriting: "))
# # #     natija = f"{son}ning kvadrati: {son ** 2}"
# # #     return natija
    
# # # print(kvadrat_fuksiya())

# # #2-savol
# # def full_name_func(first_name, last_name, name=''):
# #     if name:
# #         full_name = f"{first_name} {name} {last_name}"
# #     else:
# #         full_name = f"{first_name} {last_name}"
# #     return full_name.title() 

# # student1 = full_name_func("Muhammadyusuf", "Abdusattorov")
# # student2 = full_name_func("Husanboy", "SHermuhammedov")
# # student3 = full_name_func("Izzatbe", "Azamov")
# # student4 = full_name_func("Tohirbek", "Rustamov")
# # student5 = full_name_func("Palonchi", "Pistonchiyev", "Xojakani o'g'li")
# # print(student1)
# # print(student5)

# # # print(f"darsga kech qolgan talabalar: {student2}.\nVaqtida kelgan talabalar: {student1}, {student3}, {student4}") 

# #3-savol
# def avto_info(kampaniya, model, rangi, karobka, yili, narx=230000):
#     avto = {
#          'kampaniya': kampaniya,       
#          'model': model,   
#          'rangi': rangi,  
#          'karobka': karobka, 
#          'yili': yili,
#          'narx': narx,
#     }    
#     return avto
     
# avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020)     
# avto2 = avto_info('GM', 'Lasetti', 'oq', 'mexanik', 2018, 12000)     
# print("Online savdoda mavjud avtomabillar: ")
# for avto in [avto1, avto2]:
#     if avto['narx']:
#         print(f"{avto['yili']} {avto['kampaniya']}, avto['model], Rangi: {avto['rangi']}, Karobka: {avto['karobka']}, Narxi: {avto['narx']}")
#     else:
#         print(f"{avto['yili']} {avto['kampaniya']}, avto['model], Rangi {avto['rangi']}, Karobka: {avto['karobka']}")
        
#4-savol
def oraliq(min, max, qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam

    return sonlar

print(oraliq(1, 51, 2))
print(oraliq(10, 21, 3))
