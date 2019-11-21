message = 'Hello! This is a book'.split
#print(message)
#print(message[0])
#firstchar = message[0]
#print(firstchar[0])

list01 = [1,2,3]
list02 = ['bir',2,False,5.4]
print(list01)
print(list02)


list03 = ['bir','iki','üç']
list04 = ['dört','beş','altı']

numbers = list03 + list04
print(numbers)


userA = ['Ali',45]
userB = ['Veli',35]
users = [userA,userB]
print(users)
print(users)

# ---------------

cars = ['BMW','Mercedes','Opel','Mazda']

result = len(cars)
result = cars[0]
result = cars[1]
result = cars[2]
result = cars[-1]


result ='Ferrari' in cars
print(result)

result = cars + ['Renault','Crysler']
print(result)
del cars[-1]
print(cars)

result = cars[::-1] # Tersten sıralama
print(result)

stdA = ['Ayşecan','Tıfıl','1990',[70,60,70]]
stdB = ['Murtaza','Cibali','1992',[80,80,70]]
stdC = ['Kerimcan','Kibar','1996',[80,70,90]]


# "{AD} {SOYAD} {2019-DogumTarihi} yaşında ve not ortalaması (A+B+C)/len(NotDizi)"
 
result = f"{stdA[0]} {stdA[1]} {2019-int(stdA[2])} yaşında ve not ortalaması {(stdA[3][0] + stdA[3][1] + stdA[3][2]/len(stdA[3]))}"
result += f"{stdB[0]} {stdB[1]} {2019-int(stdB[2])} yaşında ve not ortalaması {(stdB[3][0] + stdB[3][1] + stdB[3][2]/len(stdB[3]))}"

print(result)




#List Methods

numbers = [1,2,3,4,5,6,7,8,9]
letters =['a','c','e','f','g','s']

val = min(numbers)
cal = max(numbers)

numbers[4] = 7
numbers.append(13)
print(numbers)
numbers.insert(2,9)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(-1)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.sort()
print(numbers )
