#JSON
import json

details = {
    'name':'John Doe',
    'age': 29
}

#with open() # Otomatik kendi kapatır bu close yapmana gerek yok
with open('personal.json','w') as json_file:
    json.dump(details,json_file)