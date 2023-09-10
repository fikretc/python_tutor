class Circle:
    circle_list=[]
    pi = 3.14159
    radius = 20

    def __init__(self, radius):
        self.radius = radius
        self.circle_list.append(radius)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius

c = Circle(10)
print(c.pi)
print(Circle.pi)
print(Circle.radius)
print(c.radius)
print(c.area())
print(c.circumference())
print(len(Circle.circle_list))
