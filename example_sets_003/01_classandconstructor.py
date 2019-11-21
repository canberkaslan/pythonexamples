#Tanımlama

class User:
    #def __init__(self): #Constructor
    #    self.firstname=''
    #    self.lastname=''
    #    self.username=''
    #    self.email=''
    #    self.password=''
    #    self.gender=''
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

    def __del__(self):
        print('Nesne Silindi')

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


#Kullanım

#u1 = User()
#
#u1.firstname='Canberk'
#u1.lastname='Aslan'
#u1.username='canberk_aslan'
#u1.password='123456'
#print(u1.firstname)
#print(u1.me())

u2=User('Canberk','Aslan','canberkaslan','canberkaslan@gmail.com','123456','E',1988)

#isLoggedIn = u2.login()
#if(isLoggedIn):
#    print('Giriş Başararılı')
#else:
#    print('Giriş Başarısız')
#
print(u2.__len__())

#del u2
#del u2.birthdate