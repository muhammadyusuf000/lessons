# # #1-savol
# # car0 ={
# #         "model":"gentra",
# #         "rang":"qora",
# #         "yil":2020,
# #         "narh":19000,
# #         "km":55000,
# #         "km":"avtomat"
# # }        
# # car1 = {
# #         "model":"nexia 2",
# #         "rang":"qora",
# #         "yil":2014,
# #         "narh":300000,
# #         "km":56000,
# # }

# # car2 ={
# #         "model":"BMW M5 F90",
# #         "rang":"ko'k",
# #         "yil":2024,
# #         "narh":95000000,
# #         "km":500000,
# # }

# # car = car0
# # print(f"{car['model'].title()},\
# #     {car['rang']} rang,\
# #         {car['yil']}-yil, {car['narh']}$")

# # car = car1
# # print(f"{car['model'].title()},\
# #     {car['rang']} rang,\
# #         {car['yil']}-yil, {car['narh']}$")

# # car = car2
# # print(f"{car['model'].title()},\
# #     {car['rang']} rang,\
# #         {car['yil']}-yil, {car['narh']}$")

# # cars = [car0, car1, car2]
# # for car in cars:
# #      print(f"{car['model'].title()},"
# #           f"{car['rang']} rang,"
# #           f"{car['yil']}-yil, {car['narh']}$")

# # #2-savol
cars =[]

for n in range(10):
    new_car ={
        'model':'malibu',
        'rang' :'qora',
        'yil':2013,
        'narh':140000,
        'km':23000,
        'karobka':'avto'
    }
    cars.append(new_car)
        
print(cars)

#3-savol
for car in cars[:3]:
    car['rang'] = 'yashil'
    car['narh'] = 15000

for car in cars[3:6]:
    car['rang'] = 'oq'
    car['narh'] = 20000
    
for car in cars[6:]:
    car['rang'] ='qora'
    car['narh'] = 25000

print(cars)

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#'],
    'sardor':['java','go'],
}
print(dasturchilar.keys())
print(dasturchilar.values())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')



