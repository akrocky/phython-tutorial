# -------------

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # decorator

    @classmethod
    def specific_cordinate(cls):
        return cls(1.1, 4.6)

    def walk(self):
        print(f"walking cordinates ({self.x} , {self.y})")


test_walk = Robot(1.1, 4.6)
test_walk.walk()
