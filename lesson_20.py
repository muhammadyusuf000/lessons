#1=dars
# rial_madrit={"Vinisus":23,"Belinghem":8,"Radrigo":32,"Rudiger":54,"Suars":12}
# print(rial_madrit)
# del rial_madrit["Suars"] 
# print(rial_madrit)

#2=dars
# son=1
# ismlar=[]
# while son <=5:
    # print(son, end='')
    # ism=input("Ismingizni kiriting: ")
    # ismlar.append({"id":son, "ism":ism})
    # son=son+1
# print(ismlar)

#3=dars
print("Kiritilgan sonning kvadratini qaytaruvchi dastur ")
savol="Istalgan son kiriting: "
savol+="(dasturni to'xtatish uchun 'exit' so'zini kiriting)"
qiymat=''
while qiymat !='exit':
    qiymat=input(savol) 
    qiymat=input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)