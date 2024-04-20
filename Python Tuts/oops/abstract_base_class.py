from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod

# class Shape(ABC):
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea():
        # CODE HERE----
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, l, b) -> None:
        self.length = l
        self.breadth = b

    # def printarea(self):
    #     return self.length * self.breadth
    
rect1 = Rectangle(3,4)