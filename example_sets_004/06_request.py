import json
import requests


#Example 1
#result =requests.get("https://jsonplaceholder.typicode.com/todos")
#result = json.loads(result.text)
#for  x in result:
#    if x["userId"] == 1:
#        print(x["title"])
#
#print(type(result))

#Example 2
api_url = "https://api.exchangeratesapi.io/latest?base="
bozulanDoviz = input("Döviz Türü (Bozulan) : ")
alinanDoviz = input("Döviz Türü (Alinan) : ")
miktar = int(input(f"Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz ? : "))

result = requests.get(api_url + bozulanDoviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulanDoviz,
                                result["rates"][alinanDoviz],
                                alinanDoviz))

print("{0} {1} = {2} {3}".format(miktar,
                                bozulanDoviz,
                                miktar*result["rates"][alinanDoviz],
                                alinanDoviz))