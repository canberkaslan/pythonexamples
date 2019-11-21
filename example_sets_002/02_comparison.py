result = True + False + 40

print(result)


# -----------------

email = 'canberkaslan@gmail.com'
password = 'gizli$ifre'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())
print(f'Email bilgisi doğru mu: {isEmail} ve Parola dogru mu: {isPassword}')