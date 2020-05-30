import sys

sys.path.append('../utilities')

from doubly_linked_list import DoublyLinkedList, ListNode

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

         # if buffer full and pointer not at head --no need to move pointer
        elif self.storage.length == self.capacity and self.current_pointer is not self.storage.head:
            
            self.storage.remove_from_head()

            self.storage.add_to_tail(item)

        # if buffer not full then add to tail
        else:
            self.storage.add_to_tail(item)
        

    def get(self):
        new_list = []
        first_item = self.current_pointer
        new_list.append(first_item.value)
        if first_item.next:
            next_item = first_item.next
        else:
            next_item = self.storage.head
        
        while next_item is not first_item:
            new_list.append(next_item.value)
            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        # if self.storage:
        #     new_list.append(self.current_pointer)

        # if self.current_pointer.next:
        #     self.current_pointer = self.current_pointer.next

        #     get(self)

        return new_list
'''
        # add first item
        first_item = self.current
        list_buffer_contents.append(first_item.value)
        # check to see if there is next item
        if first_item.next:
            next_item = first_item.next
        else:
            next_item = self.storage.head
        # loop through dll, appending items till done
        while next_item is not first_item:
            list_buffer_contents.append(next_item.value)
            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        return list_buffer_contents
'''

        

        # # If there is data there...
        # while self is not None:
            
        #     # add the current value in storage to the list
        #     duplicate_name_list.append(self.current_pointer)

        #     # if there is another item, set current pointer to it and add to list
        #     if self.current_pointer.next is not None:
        #         self.current_pointer = self.current_pointer.next
        #         get(self)

        #     # when down to the last item with no next...
        #     else:
        #         self.current_pointer = self.storage.head

        # print(duplicate_name_list)
        # return duplicate_name_list