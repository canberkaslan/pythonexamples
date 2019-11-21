#print(a) #Name Error

#print(10/0) #ZeroDivisionError

# Find the elements which are not contains string

list = ["12","23","21","433","13i","xyt","456"]

for x in list:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue