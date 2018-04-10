class Ab:
    a = 3

class Ac:
    a = 0

class MyFactory:
    def get_instance(self,ins):
        return ins()

if __name__ == '__main__':
    mf = MyFactory()
    print(type(mf.get_instance(Ab)))
    print(type(mf.get_instance(Ac)))