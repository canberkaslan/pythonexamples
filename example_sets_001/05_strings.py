firstname="canberk"
lastname="aslan"
age=30
greeting= 'My name is ' + firstname + lastname + 'and \nI am '+ str(age) +' years old.'
print(greeting)
length=len(greeting)
print(length)

'''print(greeting[0])
print(greeting[length-1])
print(greeting[-1])
print(greeting[2:])
print(greeting[:-5])
print(greeting[-5:])'''
print(greeting[2:30:3])

#--------------------------->

url="http://www.cihanozhan.com/guvenli-yazilim-gelistirme-owasp/"
course="Güvenli Yazilim Geliştirme:OWASP"
result = len(url)

result = url[7:10]
result = url[22:25]

result=course[::-1]#Tersten yazar
print(result)

'''

String Methods 

'''

msg = 'Hello, this is Mars!'



#result msg

print(msg)

msg = msg.upper()
print(msg)
msg = msg.lower()
print(msg)
msg = msg.title()
print(msg)
msg = msg.capitalize()

print(msg)
msg = msg.strip()

'''msg = msg.find('mars')
print(msg)
'''
isFound = msg.startswith('H')
print(isFound)
isFound = msg.endswith('!')
print(isFound)