#на основе класса треугоника  нужно создать класс равносторонний 

class Triangle:
    def __init__(self, height1, height2,height3):
      self.height1 = height1
      self.height2 = height2
      self.height3 = height3
   
    @property
    def perimetr(self):
        return (self.height1 + self.height2 + self.height3)


class Edu_triangle(Triangle):
   def __init__(self, height):
      super().__init__(height,height,height)

fig1 = Triangle(2,4,6)
fig2 = Edu_triangle(9)

print(fig1.perimetr)
print(fig2.perimetr)