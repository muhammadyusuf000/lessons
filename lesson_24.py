# # # # # def ozim_haqimda(ism, yosh, t_yil, joylashuv):
# # # # #     """Salom beruvchi funksiya
# # # # #     """
# # # # #     print(f"Assalomu alaykum hurmatli {ism.title()}, siz {t_yil}-da {joylashuv}da tug'ilgansiz. yoshingiz {yosh}da.")
# # # # # ozim_haqimda("muhammadyusuf", 15, 2011, "oltiariq")
# # # # # ozim_haqimda("izzatxon", 5, 2025, "oltiariq")

# # # # # #2-savol
# # # # def yosh_hisobla(ism, yil):                      
# # # #     print(f"Assalomu alaykum, hurmatli {ism.title}, siz {2025-yil} yoshdasiz.")
# # # # yosh_hisobla(yil=2011, ism="Muhammadyusuf")
    
# # # #3-savol
# # # def son_darajasi():
# # #     son = int(input("Istalgan son kiriting: "))

    
# # #     kvadrat = son ** 2
# # #     kub = son ** 3
# # #     print(f"{son} ning kvadrati {kvadrat}, kubi esa {kub} ga teng.")
    
# # # son_darajasi()

# # # #4-dars    
# # def son_darajasi():
# #     son = int(input("Istalgan son kiriting: "))


# #     if son%2==1:
# #         print(f"{son} soni toq son.")
# #     else:
# #         print(f"{son} soni juft son.")

# # son_darajasi()

# # #5-dars
# def kattasi():
#     son1 = int(input("Istalgan son kiriting 1: "))    
#     son2 = int(input("Istalgan son kiriting 2: "))    

#     if son1 > son2:
#       print(f"{son1} soni katta son.")
      
#     elif son1 == son2:
#       print("Bu sonlar o'zaro teng.")
      
#     else:  
#       print(f"{son2} soni katta son.")
      
# kattasi()  

#6-dars
def darajasi():
    """x sonini y darajasi hisoblaydigan funksiya"""
    x = int(input("X sonini kiriting: "))
    y = int(input("Y sonini kiriting: "))
    return x ** y

print(darajasi()) 