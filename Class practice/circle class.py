class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  def __repr__(self):
    return 'Circle with radius {radius}'.format(radius = self.radius)
  def all(self):
      return 'the area is {area}, the circumfrence is {c} and the radius is {r}.'.format(area = Circle.area(self), c = Circle.circumference(self), r =Circle.__repr__(self))
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)