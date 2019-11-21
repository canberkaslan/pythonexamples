import sys
x = "10"
y = "20"
print(x + y)

'''
adsoyad=7
hebe=5
'''

person1 = 5000
person2 = 4000
tax = 0.2

print(person1 -(person1*0.2))
print(person2 -(person2*0.2))


fname=20
FNAME=30
print(fname)
print(FNAME)


yas = 30 # Public olarak

_yas = 30 # Classlarda privat variable olarak kullandıklarında bu şekilde olur.


isStudent = True
print(isStudent)


ondalik=4.5
print(ondalik)


'''
    Unlu bir rapcinin tenek kişisel bilgilerini alan bir değişken uygulaması
        
        FirstName   : Tupac
        Lastname    : Shakur
        FullName    : Tupac Shakur
        Gender      : Erkek
        SSN         : 54883294823-8454
        YearOfBirth : 1971
        YearOfDeath : 1996
        Address     : New York
        Age         : ?
'''


firstname= input("Please Enter name?")
lastname= input("Please Enter lastname?")
gender = input("Please Enter Gender?(E/K)")
while gender != "E" and gender != "K" and  gender != "k" and gender != "e":
    gender = input("Please Enter Correct Gender?(E/K)")
ssn = input("Please Enter SSN?")
yearofbirth = input("Please Enter date of birth?")
yearofdeath = input("Please Enter  date of  death?")
address = input("Please Enter  address?")
age=int(yearofdeath)-int(yearofbirth)

print("FirstName: {} ".format(firstname))
print("Lastname: {} ".format(firstname))
print("FullName: {} {} ".format(firstname,lastname))
print("Gender: {}".format(gender))
print("SSN: {}".format(ssn))
print("Year Of Birth: {}".format(yearofbirth))
print("Year Of Death: {}".format(yearofdeath))
print("Address: {} ".format(address))
print("Age: {}".format(age))


