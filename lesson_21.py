# cars = { "name" : "bmw" , "color": "black", "year": 1996, "price":20000} 
# rang = cars["color"]
# yili = cars["year"]
# narx = cars["price"]

# print(f"Mening mashinam rangi {rang}, yili {yili}, narxi {narx} dollar.")

#2-savol
# about_me = {"firstname":"Behruzbek","last name":"Asadullayev","year":"14 yosh", "jobs":"afitsant","school":"maktab"}
# ism=about_me["name"]
# familya=about_me["last name"]
# yilim=about_me["year"]
# ishim=about_me["jobs"]
# maktab=about_me["36-maktab"]
# print(f"mening ismim{ism},familiya{familya},yili{year}daman,jobs{jobs},maktab{maktab}da oqiyman")
# print(about_me.items())

# for k, q in about_me.items():
    # print(f"Kalit: {k}")
    # print(f"Qiymat: {q}")
    
# about_me = {"firstname":"Behruzbek","last name":"Asadullayev","year":"14 yosh", "jobs":"afitsant","school":"maktab"}

# print(about_me.keys())    

# bozorlik = ["banan","non", "qaymoq", "sut", "tarvuz", "guruch", "kartoshka", "sabzi", "go'sht",]
# mahsulotlar = {"non": 5000, "qaymoq": 20000, "sut": 25000, "tarvuz": 15000, "sabzi": 5000, "go'sht": 120000}
    
# for mahsulotlar in mahsulotlar:
    # if mahsulot in bozorlik:
        # print(f"{mahsulot,title()}, narx {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
    # if buyum not in mahsulotlar:
        # print(f"Iltimos, do'koningizga {buyum} ham olib keling")


bozorlik = ["banan","non", "qaymoq", "sut", "tarvuz", "guruch", "kartoshka", "sabzi", "go'sht",]
mahsulotlar = {"non": 5000, "qaymoq": 20000, "sut": 25000, "tarvuz": 15000, "sabzi": 5000, "go'sht": 120000}


# print(mahsulotlar.keys())  
# print(mahsulotlar.values())

for narx in mahsulotlar.values():
    print(f"Mahsulot narxlari: {narx}")
    
davlatlar = {"Rassiya":"Maskva","Uzbekistan":"Toshkend","Angliya":"London","Turkiya":"Anqara","Yaponiya":"Tokiyo"}
for davlat, poytaxt in davlatlar.items():   
    print(f"{davlat} davlatning poytaxti {poytaxt} shahri")