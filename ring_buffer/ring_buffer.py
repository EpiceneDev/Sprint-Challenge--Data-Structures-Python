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
        # if buffer is empty, add item to head and set the pointer to head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current_pointer = self.storage.head

        # when buffer is full and pointer is at head:
        elif self.storage.length == self.capacity and self.current_pointer is self.storage.head:
            # remove from head
            self.storage.remove_from_head()
            # add item to tail
            self.storage.add_to_tail(item)
            # set item at tail as current item
            self.current_pointer = self.storage.tail

    def get(self):
        pass