#names = ['ali','veli','murtaza']
#for x in names: 
#    print(f'my name is {x}')
#
#name = 'Cabbar Can'
#
#for x in name:
#    print(x)
#

#tuple = [(1,2),(3,4),(5,6),(7,8)]
#for x in tuple:
#    for y in x:
#        print(y)
#tuple = [(1,2),(3,4),(5,6),(7,8)]
#for x,y in tuple:
#        print(x,y)
#
#x = {'x1':1,'x2':2,'x3':3,'x4':4} # Dictionary
#for key,value in x.items():
#    print(key)
#    print(value)

urunler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}
]

# Ürün fiyatlarının toplamını bulun

toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('toplam ürün fiyatı : ', toplam)
    
