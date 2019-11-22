# Decorators
# Decorator Definition
def myDecorator(func):
    def wrapper(name):
        print("Doing things that before function")
        func(name)
        print("Doing things that after function")
    return wrapper

#Usage of Decorator
@myDecorator
def sayHello(name):
    print("hello",name)

#
sayHello("ABC")