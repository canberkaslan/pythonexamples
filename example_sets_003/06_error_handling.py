#print(a) #Name Error

#print(10/0) #ZeroDivisionError

# Find the elements which are not contains string

list = ["12","23","21","433","13i","xyt","456"]

for x in list:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

def checkPassword(parola):
    tr_chars ="İıöçşüğ"
    for x in parola:
        if x in tr_chars:
            raise TypeError('Parola TR karakteri içermemelidir')
        else:
            pass
    print('Şifre Gecerlidir')

#Usage
pwd = input('Parola Giriniz:')

try:
    checkPassword(pwd)
except TypeError as err:
    print(err)