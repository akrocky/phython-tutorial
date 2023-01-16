# -------------instance vs class attribute

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking cordinate ({self.x},{self.y})")


test_walk1 = Robot(8.9, 9.9)
test_walk1.walk()
