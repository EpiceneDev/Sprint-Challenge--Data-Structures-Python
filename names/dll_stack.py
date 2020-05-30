# import sys
# sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

# FILO = LIFO
class Stack:
    def __init__(self): 
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1

        popped_value = self.storage.remove_from_tail()

        return popped_value
        # if self.size > 0:
        #     value = self.storage.remove_from_head()
            
        #     self.size -=1
            
        #     return value

        # else:
        #     print("The stack is empty.")

