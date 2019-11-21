class User:
   
    def __init__(self,fname,lname,uname,ema,passwd,gndr,yearOfBirth):
        self.firstname=fname
        self.lastname=lname
        self.username=uname
        self.email=ema
        self.password=passwd
        self.gender=gndr
        self.birthdate=yearOfBirth
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __len__(self):
        return 2019 - self.birthdate

    def me(self):
        return 'My name is {} {}'.format(self.firstname,self.lastname)
    
    def register(self):
        print('Registered')

    def login(self):
        self.age = 5
        print(self.age)
        result=False
        if(self.email =='canberkaslan@gmail.com' and self.password == '123456'):
            result =True
            return result
        else:
            return result
    def logout(self):
        print('logout')

class Student(User):  #kalıtımı boyle yapıyoruz
    
    def __init__(self,fname,lname,uname,ema,passwd,gndr,yearOfBirth,number):
        User.__init__(self,fname,lname,uname,ema,passwd,gndr,yearOfBirth) #User class ına aldıgım parametreleri set ediyor
        self.studentNumber=number
        print('Student Created')

class Teacher(User):  #kalıtımı boyle yapıyoruz
    def __init__(self,fname,lname,uname,ema,passwd,gndr,yearOfBirth,branch):
        User.__init__(self,fname,lname,uname,ema,passwd,gndr,yearOfBirth) #User class ına aldıgım parametreleri set ediyor
        self.branch=branch
        print('Teacher Created')

s1 = Student('Ayse','Cici','aysecici','aysecici@gmail.com','12345','K',2001,324234)
print(s1.me())
t1 = Teacher('Ahmet','Tek','ahmettek','ahmet.tek@gmail.com','67890','E',1975,'Matematik')
print(t1.me())
#u1 = User()
#u1.firstname = 'Ali'
#print(u1.firstname)
#
#s1 = Student()
#s1.firstname='Ayşe'
#
#print(s1.firstname)