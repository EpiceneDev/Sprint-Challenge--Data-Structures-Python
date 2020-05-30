# import sys
# sys.path.append('../queue_and_stack')

from dll_queue import Queue
from dll_stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            # check to see if right exists
            if self.right:
            # if so, make that node call insert with the same value
                self.right.insert(value)
            ## if not, create a node with hthat value, set node as right child
            else:
                self.right = BSTNode(value)
        else:
            # check if left exists
            if self.left:
            # if so, make the node and insert the same value
                self.left.insert(value)

            #if not, create a node right here
            else:
                new_node = BSTNode(value)
                self.left = new_node



        # compare value to the current node
        # if value < self.value and self.left is None:
        #     self.left = BSTNode(value)
        #     return
        # elif value >= self.value and self.right is None:
        #     self.right = BSTNode(value)
        #     return
        # if value < self.value:
        #     self.left.insert(value)
        # else:
        #     self.right.insert(value)
        # if smaller, go left
            # if value < node.value look left
                # if something is there already
                # recurse left
            # if not
                # insert left
        # if bigger look right
        # if something is there
            # recureseleft
        # if no node, make one at that spot
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            
            else:
                return False

        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right
        
        return current_node.value
        # if self.right is None:
        #     return self.value
        # return self.right.get_max()


# TRAVERSAL
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left FIRST
        if self.left:
            self.left.for_each(cb)
        
        # go right
        if self.right:
            self.right.for_each(cb)

        # post order here
        cb(self.value)

        # return None # will do this by default if not told... goes back to parent

# node_10 = BSTNode(10)
# node_10.for_each(print)

# #recursion is much like a call stack
# 10, 8, 7, 9, 12, 11, 13


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left FIRST
        if node.left:
            node.in_order_print(node.left)

        # Print ourselves
        print(str(node.value))

        # go right 
        if node.right:
            node.in_order_print(node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal
    def bft_print(self, node):

        if node is None:
            return

        #create a queue for nodes
        node_queue = Queue()
        #add current node to queue
        node_queue.enqueue(node)
        #while the queue is empty
        while node_queue.size > 0:
            #dequeue node

            temp = node_queue.dequeue()
            #print node
            print(temp.value)
            # add node children
            if temp.left:
                #if left, add 
                node_queue.enqueue(temp.left)
            if temp.right:
                #if right, add
                node_queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return

        # create a node_stack
        node_stack = Stack()
        # push the current node onto stack
        node_stack.push(node)
        # while we have items on stack
        while node_stack.size > 0:
            # print the current value and pop it off

            temp = node_stack.pop()
            print(temp.value)
            # push the right value of the current node if we can
            if temp.right:
                node_stack.push(temp.right)

            # push the left value of current node if we can
            if temp.left:
                node_stack.push(temp.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return

        else:
            print(node.value)

            self.pre_order_dft(node.left)

            self.pre_order_dft(node.right)



    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return

        else:
            self.post_order_dft(node.left)

            self.post_order_dft(node.right)

            print(node.value)