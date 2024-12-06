class Circle:
    circle = "круг"
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return "Радиус круга: {}".format(self.radius)

    def new_radius(self, new_radius):
        self.radius = new_radius
cir = Circle(123)

def foo():

    cir.new_radius(int(input("Введите радиус круга: ")))
    return print(cir.get_radius()), foo()
foo()