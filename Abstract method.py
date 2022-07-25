from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,value,value2):
        self.value=value
        self.value2=value2
    @abstractmethod
    def area(self):
        pass
    """jokon kono method a body dewa hobe na ,tokon takhe abstract method bole"""
"""karon ai method k je kaw essa moto use korte parbe"""
class triangle(shape):
     def area (self):
        area=0.5 * self.value*self.value2
        print(area)

class rectanghular(shape):
    def area(self):
        area=self.value*self.value2
        print(area)
"""shape abstract class that's why shape ar object create kora jabe na"""
r=rectanghular(5,8)
r.area()

t=triangle(6,6)
t.area()
