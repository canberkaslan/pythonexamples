#1 - 100 e kadar

#x = 1
#while x <= 100:
#    if x % 2 ==1:
#        print(f'sayi tek: {x}')
#    else:
#        print(f'sayi çift: {x}')
#    x+=1
#
#
#name = ' '
#while name.isspace():
#    name = input('enter name:')


#name = ' '
#while not name.isspace():
#    name = input('enter name:')


products = []
productCount = int(input('Product Count:'))

x = 0 

while(x < productCount):
    name = input('Product Name: ')
    price = input('Product Price:')
    products.append({
        'name': name,
        'price':price
    })
    x+=1

for p in products:
    print(f'****************')
    print(f'Product Name: {p["name"]}')
    print(f'Product Price: {p["price"]}')
    print(f'****************')