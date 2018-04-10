class Singleton(object):
    _sg1 = None
    def __new__(cls,*args,**kwargs):
        if not cls._sg1:
            cls._sg1 = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._sg1

class MyClass(Singleton):
    a = 1

if __name__ == '__main__':
    sa = MyClass()
    sb = MyClass()
    print(id(sa))
    print(id(sb))