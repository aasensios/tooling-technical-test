'''Tests should be made to ensure that the class FIFO works as expected.'''

from datetime import datetime
from fifo import FirstInFirstOut

FIRST_ELEMENT = 'foo'
SECOND_ELEMENT = 'bar'
get_elements = lambda queue: (element for (element, _) in queue)

def test_addition_and_size():
    '''Check queue size before and after adding elements to it.
    Also check the presence of each element after its addition.'''
    fifo = FirstInFirstOut()
    assert fifo.size() == 0
    fifo.push(FIRST_ELEMENT)
    assert fifo.size() == 1 and FIRST_ELEMENT in get_elements(fifo.queue)
    fifo.push(SECOND_ELEMENT)
    assert fifo.size() == 2 and SECOND_ELEMENT in get_elements(fifo.queue)


def test_removal_and_size():
    '''Check queue size before and after removing elements from it.
    Also check the presence of each element after its addition and its
    non-presence after its removal.
    Finally, check each popped element corresponds to the current oldest
    element in the queue.'''
    fifo = FirstInFirstOut()
    assert fifo.size() == 0
    fifo.push(FIRST_ELEMENT)
    assert fifo.size() == 1 and FIRST_ELEMENT in get_elements(fifo.queue)
    fifo.push(SECOND_ELEMENT)
    assert fifo.size() == 2 and SECOND_ELEMENT in get_elements(fifo.queue)
    oldest_element = fifo.pop()
    assert oldest_element[0] == FIRST_ELEMENT and FIRST_ELEMENT not in get_elements(fifo.queue)
    oldest_element = fifo.pop()
    assert oldest_element[0] == SECOND_ELEMENT and SECOND_ELEMENT not in get_elements(fifo.queue)


def test_addition_time_with_and_without_position():
    '''Check addition_time method with and without specifiying the position
    of the element in the queue.
    If no position is specified the addition_time methos should return the
    last addition.'''
    fifo = FirstInFirstOut()
    fifo.push(FIRST_ELEMENT)
    fifo.push(SECOND_ELEMENT)
    first_addition_time = fifo.addition_time(-1)
    second_addition_time = fifo.addition_time(-2)
    last_addition_time = fifo.addition_time()
    assert isinstance(first_addition_time, datetime)
    assert isinstance(second_addition_time, datetime)
    assert isinstance(last_addition_time, datetime)
    assert first_addition_time != second_addition_time
    assert second_addition_time == last_addition_time
