import sys

sys.path.append('./doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

# a ring buffer is a type of queue: FIFO
# stores in fixed size array
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # This is the size of the buffer
        self.current_pointer = None # Using this for temp storage
        self.storage = DoublyLinkedList()

    def append(self, item):
        

    def get(self):
        pass