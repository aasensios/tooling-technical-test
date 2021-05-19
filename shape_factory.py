'''Implement a Factory (design pattern) about shapes (circle, square, rectangle).'''

class Shape():
    '''Shape interface.'''
    def draw(self, shape, emoji) -> None:
        '''Specific shape and custom emoji should be provided by child classes.'''
        print(f'\nA {shape} {emoji} has been drawn', end='')

class Circle(Shape):
    '''Circle class.'''
    def draw(self) -> None:
        super().draw('circle', '🔵')

class Square(Shape):
    '''Square class.'''
    def draw(self) -> None:
        super().draw('square', '🟧')

class Rectangle(Shape):
    '''Rectangle class.'''
    def draw(self) -> None:
        super().draw('rectangle', '💳')

class ShapeFactory():
    def get_shape(shape_type: str) -> Shape:
        if shape_type == 'circle':
            return Circle()
        if shape_type == 'square':
            return Square()
        if shape_type == 'rectangle':
            return Rectangle()
        return None
