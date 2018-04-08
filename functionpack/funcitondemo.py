

def myfunc(name):
    print("This is my first function.")
    print("I'm %s" % name)


def mynewfunc(name='Tom',age=18, *args, **kwargs):
    print("This is my seconde function.")
    print("I'm %s,%s years old" % (name,age))
    print(args)
    print(kwargs)
    return 'hello'



myfunc("Maggie")

hello = mynewfunc("kim",30,12,43,212,sex='man',cc='xix')

print(hello)