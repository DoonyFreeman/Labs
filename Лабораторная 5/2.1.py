


class Circle:
    circle = "круг"
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return "Радиус круга: {}".format(self.radius)

    def new_radius(self, new_radius):
        self.radius = new_radius

cir = Circle(123)
cir.new_radius(15)
print(cir.get_radius())