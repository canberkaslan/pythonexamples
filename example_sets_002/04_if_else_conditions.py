#x=float(input("bla bla "))

#if x >50:
#    print("Elli - elliden büyük")


#uname='canberkaslan'
#pwd = '1234!'

#if (uname == 'canberkaslan'):
#    if (pwd == '1234!'):
#        print('Hosgeldiniz')
#    else:
#        print('Parola yanlis')
#else:
#    print('Kullanıcı adı yanlis')

# if-elif-else

#x = int(input('X:'))
#y = int(input('Y:'))
#
#if x > y:
#    print("x y den büyük")
#elif x < y:
#    print ("x y den kucuk")
#else:
#    print("x y ye eşit")


ortalama,basarili,final = 30 ,True,60
if (ortalama >=50):
    basarili=True
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu {basarili}')
else:
    if(final>=70):
        basarili=True
        print(f'Öğrencinini ortalaması {ortalama} ve geçme durumu {basarili}. Finalden aldıgı not ile geçmiştir')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu {basarili}') 