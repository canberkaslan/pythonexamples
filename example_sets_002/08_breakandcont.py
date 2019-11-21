# 1-100 e kadar tek sayıların toplamı

x,result=0,0
while x<=100:
    x+=1
    if x %2 ==0 :
        continue
    result += x

print(f'Toplam Sonuc: {result}')

# Girilen bir sayının asal olup olmadığını bulan kod 
sayi = int(input('sayı:'))
asalMi=False
if sayi==1:
    asalMi

for i in range(2,sayi):
    if(sayi %i == 0):
        asalMi = False
        break
if asalMi:
    print('Sayi asaldir')
else:
    print('Sayi asal degildir') 