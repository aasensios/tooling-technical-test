'''Implement a Factory (design pattern) about shapes (circle, square, rectangle).'''

# pylint: disable=R0903

class Shape():
    '''Shape interface.'''
    @staticmethod
    def draw(shape_type, emoji) -> None:
        '''Specific shape and custom emoji should be provided by child classes.'''
        print(f'\nA {shape_type} {emoji} has been drawn', end='')

class Circle(Shape):
    '''Circle class.'''
    def draw(self, shape_type='circle', emoji='🔵') -> None:
        super().draw(shape_type, emoji)

class Square(Shape):
    '''Square class.'''
    def draw(self, shape_type='square', emoji='🟧') -> None:
        super().draw(shape_type, emoji)

class Rectangle(Shape):
    '''Rectangle class.'''
    def draw(self, shape_type='rectangle', emoji='💳') -> None:
        super().draw(shape_type, emoji)

class ShapeFactory():
    '''Shape factory.'''
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        '''Instantiate a different class regarding the shape type.'''
        if shape_type == 'circle':
            return Circle()
        if shape_type == 'square':
            return Square()
        if shape_type == 'rectangle':
            return Rectangle()
        return None
