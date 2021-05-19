'''Tests for the Factory design pattern about shapes (circle, square, rectangle).'''

from shape_factory import ShapeFactory, Shape, Circle, Square, Rectangle


def test_circle():
    '''Check the shape factory for a circle.'''
    circle = ShapeFactory.get_shape('circle')
    circle.draw()
    assert isinstance(circle, Circle)
    assert isinstance(circle, Shape)


def test_square():
    '''Check the shape factory for a square.'''
    square = ShapeFactory.get_shape('square')
    square.draw()
    assert isinstance(square, Square)
    assert isinstance(square, Shape)


def test_rectangle():
    '''Check the shape factory for a rectangle.'''
    rectangle = ShapeFactory.get_shape('rectangle')
    rectangle.draw()
    assert isinstance(rectangle, Rectangle)
    assert isinstance(rectangle, Shape)
