def sayHello():
    print('Hello World')
# Private function implementation 
def outer(p1):
    print('Outer')
    def inner(p2):
        print('inner')
        return p2+2
    res = inner(p1)
    print(res)


outer(5)