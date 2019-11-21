#def sayHello (name = '{unknown}'):
#    print('Hello'+ name)
#
#
#sayHello('canberk')
#sayHello()
#
#
#def BirMethod(input1,input2):
#    '''
#        DOCSTRING : ACIKLAMA
#        INPUT1 : DSMFPMDFS
#        INPUT2 : LDMFSMDF
#    '''
#    print('çıktı')
#
#BirMethod(2,3)
#
#
#print(help(BirMethod))


#istediğim kadar parametre ile fonksıyon cagırma

#def listeyeCevir(*params):
#    liste = []
#    for param in params:
#        liste.append(param)
#    return liste
#
#result = listeyeCevir(10,20,39,'Hello!')
#
#print(result)


def add(*params): # tek yıldız tuple 
    print(type(params))
    sum = 0
    for n in params:
        sum =sum +n
    return sum
#  variadic parameters
print(add(5,10,15))


def displayUser(**args): # cıft  yıldızda dırectory olarak
    print(type(args))
    for key,value in args.items():
        print('{} is {}'.format(key,value))


displayUser(name='canberk',age=31,city='istanbul')


def funct1(x,y,z,*args, **kwargs): # kwargs -> keyword args
    print(x)
    print(y)
    print(z)
    print(args)
    print(kwargs)

funct1(10,20,30) # x,y,z ye gider

funct1(10,20,30,40) # args a gider

funct1(10,20,30,40,50) # args a gider

funct1(10,20,30,40,key1 ='value1',key2='value2') # kwargs a ve args a  gider



