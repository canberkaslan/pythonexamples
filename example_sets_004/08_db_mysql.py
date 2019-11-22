import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root"
    password = "şifre!",
    database = "node-app"
)

mycursor = mydb.cursor()

sql ="select * from dual"
cursor.execute(sql)
try:
    connection.commit()
    print(f'{cursor.rowCount} tane kayıt var')
except mysql.connector.Error as err:
    print("Hata:",err)
finally:
    connection.close()
    print("database baglantısı kapandı")