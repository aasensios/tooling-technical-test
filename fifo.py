'''Implement a class FIFO (First In First Out).'''

from datetime import datetime

class FirstInFirstOut:
    '''It should be a class with the following methods: push, pop, size, addition_time.'''
    def __init__(self) -> None:
        self.queue = []

    def push(self, element) -> None:
        '''Add an element at first position.
        Also store the datetime when the addition occurs.
        To achieve that, a tuple (element, datetime) is stored.'''
        self.queue.insert(0, (element, datetime.today()))

    def pop(self) -> tuple:
        '''Get and remove the oldest element.
        The oldest element is placed at the last index of the queue list.'''
        return self.queue.pop()

    def size(self):
        '''Get the number of elements.'''
        return len(self.queue)

    def addition_time(self, position: int = 0):
        '''Get the datetime when any element present on the FIFO was added.
        If no position is specified by default return the last element
        addition.'''
        return self.queue[position][1]
