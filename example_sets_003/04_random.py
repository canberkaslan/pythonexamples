import random
names = ['ali','canberk','ahmet','veli','hakan']
result = names[random.randint(0,len(names)-1)]
print(result)


liste = list(range(10))
print(liste)
random.shuffle(liste)
print(liste)

