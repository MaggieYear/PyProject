

def myfunc(name):
    print("This is my first function.")
    print("I'm %s" % name)


def mynewfunc(name='Tom',age=18, *args, **kwargs):
    print("This is my seconde function.")
    print("I'm %s,%s years old" % (name,age))
    print(args)
    print(kwargs)
    return 'hello'

def func(x):
    return (x>3)

#print(filter(func,[1,2,3,4,5]))

#print(filter(lambda x:x>3,[1,2,3,4,5]))

#print(map(lambda x:x+x,[1,2,3,4,5]))

#print(reduce(lambda x:x+x,[1,2,3,4,5]))

print(reduce(lambda x, y: x+y, [1,2,3,4,5]))

print(filter(lambda x:len(x)==0,'hello'))

#myfunc("Maggie")



#hello = mynewfunc("kim",30,12,43,212,sex='man',cc='xix')

#print(hello)