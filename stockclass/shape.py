
class shape:
    def __init__(self , color):
        self. colour = color
    def get_area(self):
        ...

class Rectangle(shape):
    def __init__(self ,colour, length, breath):
        super().__init__(colour)
        self._length = length
        self._breath = breath
    def get_area(self):
        return self._length * self._breath

    