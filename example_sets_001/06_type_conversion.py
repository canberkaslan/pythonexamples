'''
x = input('1. Sayı : ')
y = input('2. Sayı : ')

print(type(x))
print(type(y))


result = int(x) + int(y)

print(result)
print(type(result))'''

x = 7 
y = 7.5
name ="Ceza"
isOnline = True

#x = float(x)
#print(x , type(x))

#implicit conversion
result = x + y
print(type(result), result) 

y= int(y)
print(y)
#Boolean to string
#print(type(isOnline))
#isOnline = str(isOnline)
#print(type(isOnline))

# Boolean to int
'''
isOnline= False
print(isOnline)
print(type(isOnline))
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
'''
'''
    Daire Alanı
    Daire Çevresi
    - Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız
    r: 3.14
'''
pi=3.14
yaricap= input("Lütfen yarıçapı giriniz ? ")
yaricap = float(yaricap)
alan = pi*yaricap*yaricap
print('Daire Alanı :' , alan)
cevre = 2*pi*yaricap
print('Daire Çevresi :' , cevre)
