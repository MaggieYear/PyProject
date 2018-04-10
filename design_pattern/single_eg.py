class SingleClass:
    def __init__(self):
        self.x = 0

sc = SingleClass()

def tsc():
    print(sc.x)
    sc.x = 10
    print(sc.x)

def tsc2():
    print(sc.x)
    sc.x = 9
    print(sc.x)

if __name__ == '__main__':
    tsc()
    tsc2()