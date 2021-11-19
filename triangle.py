class Triangle:
    def __init__(self, height, base):
        self.height=height
        self.base=base
        
    def triangar(self):
        triangar=0.5*self.height*self.base
        return triangar

my_triangle=Triangle(2,3)
print(my_triangle.triangar())