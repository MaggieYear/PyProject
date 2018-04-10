class Moveable:
    def move(self):
        print("move...")

class MoveOnFeet(Moveable):
    def move(self):
        print("move on feet...")

class MoveOnWheels(Moveable):
    def move(self):
        print("move on wheels...")

class Moveobj:
    def set_move(self,moveable):
        self.moveable = moveable()

    def move(self):
        self.moveable.move()


if __name__ == '__main__':
    m = Moveobj()
    m.set_move(Moveable())
    m.move()
    m.set_move(MoveOnFeet())
    m.move()
    m.set_move(MoveOnWheels())
    m.move()