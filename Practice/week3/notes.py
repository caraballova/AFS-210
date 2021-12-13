def strangeFunction(items) :    
    for i in range (5,0,-1) :               # O(5)
        print('Staring in ', i)

    for item in items:
        print(item, end=" ")                # O(n)

    print()                                 # O(1)

    for x in range (0,len(items),2) :       # O(n/2)
        print(items[x], end=" ")

    print("\nFinished")

strangeFunction([3, 5, 8, 10, 32, 18])      # O(5)+O(n)+O(1)+O(1/2n)+O(1)=O(n)

from collections import deque 

# Deque is short for Double Ended Queue.  It is a hybrid between a Stack and a Queue providing 
# the functionality of both in one data structure.
#
# The time complexity of adding or removing an item on either side of a deque 
# takes constant time O(1).
#
# Deque Operations:
# append(item)          : Insert the item to the right end of deque.  Same as stack "push" method
# appendleft(item)      : Insert the item to the left end of deque.  Same as queue "enqueue" method
# insert(index,item)    : Insert the item at the given index
# pop()                 : Delete an item from the right end of deque.  Same as the stack "pop" method
# popleft()             : Delete an item from the left end of deque. Same as queue "dequeue" method
# remove(item)          : Remove the first occurrence of the item
# count(item)           : Return the total number of occurrences of the given value
# rotate(n)             : Rotate the deque n number of times.  
#                         A positive value rotates to the right
#                         A negative value rotates to the left
# reverse()             : Reverse the order of the deque


#                 Deque
#  <---- Left Side     Right Side ---->
#
# -------------------------------------
# |  1  |  2  |  3  |  4  |  5  |  6  |
# -------------------------------------
#
#  <---- Queue Like     Stack Like ---->

months = deque(['February','March','April','June','July','August','September','October', 'November'])
months.append('December')
months.appendleft('January')

print(months)

months.append('At The End')         # adds an item to the right end of the deque
months.appendleft('At the Front')   # adds an item to the left end of the deque
months.pop()                        # deletes item from the right end of deque
print(months)
months.popleft()                    # delete an item from the left end of deque
print(months)

months.rotate(4)
print(months)

months.rotate(-2)
print(months)

# Binary Search Tree

# – A tree where each node can have at most two children, often referred to as left and right child.
                
# Binary Search Tree
# - For a given node with a value, all the nodes in the left sub-tree are less than or equal 
# to the value of that node. While, all the nodes in the right sub-tree of this node are greater
# than that of the parent node.   

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return

bsTree = BinaryTree()
bsTree.insert(5)
bsTree.insert(3)
bsTree.insert(6)

