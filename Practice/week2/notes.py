# Recursion - A method of solving a problem by breaking the problem down into smaller and smaller subproblems until a simple solution is found.
# A recursive function is one that calls itself from within its own code
# Data between recursive calls is stored on a stack

# Sum of n numbers
# Given a positive integer value, n, find the sum of all integers between 0 and n, including n.
# If n = 7, then the summation is 28
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# Iterative Function

def loopSum(n) :
    sum = 0                             # Initial value of zero
    for x in range (1, n+1) :           # Start at 1 and include n
        sum += x                        # At current value to sum
        return sum                      # Return the sum of n integers

n = 7                                   # 1 + 2 + 3 + 4 + 5 + 6 + 7
print(loopSum(n))                       # Output: 28

# Recursive Function

def recSum(n) :
    if n <= 1 :                         # Base case
        return n                        # return 1
    return n + recSum(n-1)              # Call ourself and move towards base case

n = 7                                   # 1 + 2 + 3 + 4 + 5 + 6 + 7
print(recSum(n))                        # Output: 28



# Three parts of a Recursive Algorithm
    # 1. Must have a base case - base case stops the recursion
    # 2. Must move towards the base case by changing the state
    # 3. Recursively call itself

# Recursion                                         vs                                      Iteration

# Function calls itself                                                                     Implemented using loops
# Terminates when a base case is reached                                                    Terminates when a defined condition is met
# Each recursive call requires space in memory                                              Each iteration is not shared in memory
# Slower due to overhead of maintaining the stack of calls                                  Faster without the need to maintain a stack of calls
# Some problems are naturally better suited to recursive solutions                          Iterative solutions may not alwas be obvious


# Converting Iterative Loop into a Recursive Loop

# The factorial function says to multiply all whole numbers from a chosen number down to 1.
# if n = 3, then we have 3 * 2 * 1 = 6
# If n = 5, then we have 5 * 4 * 3 * 2 * 1 = 120
# If n = 8, then we have 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320

# Three Parts of a Recursive Algorithm
    # 1. Must have a base case – base case stops the recursion
    # 2. Must move towards the base case by changing the state
    # 3. Recursively call itself

# Iterative loop factorial function

def factorial(x):
    retVal = x
    for i in reversed(range(1,x)):
        retVal *= i
    return retVal

n = 3
print(factorial(n))

# Iterative Function

def factorialLoop(x):
    retVal = x
    for i in reversed(range(1,x)):
        retVal *+ i
        return retVal

# Recursive Function

def factorial(x) :
    if x == 1:
        return 1                        # creating the base case
    else:
        return(x * factorial(x-1))      # recursive calls itself & changing the state

n = 5
print(factorialLoop(n))
print(factorial(n))

# Iterative Loop

def countDown():
    for i in range(10,0,-1):
        print(i)
    print("Blast Off!!!!")


# Recursive Algorithm

def blastOff(i):
    if (i==0):
        print("---Blast Off!!")
    else:
        print(i)
        blastOff(i-1)

countDown()
blastOff(10)

# Big-O Notation
# When analyzing an algorithm, there are three cases to consider when estimating its theoretical complexity
    # Best case(Big Omega or Ω(n)) - Least important
    # Average case (Big Theta or Θ(n)) - Sometimes necessary
    # Worst case (Big O or O(n)) - Most important !

# Gives us a way to calculate the complexity, both time and space, of an algorithm in terms of the input size, N.
# The calculation is independent of the machine.
# Big-O is notated by O(n) the represents and the relationship between the input and the steps taken by the algorithm (n)

# Complexity Class                                  Name                                Example Operation
# O(1)                                              Constant                            append, get item, set item
# O(logn)                                           Logarithmic                         Finding an element in a sorted array
# O(n)                                              Linear                              copy, insert, delete, iteration
# O(nLogn)                                          Linear-Logarithmic                  sorting a list, merge-sort
# O(n^2)                                            Quadratic                           Find the shortest path between two nodes in a graph. Nested loops
# O(n^3)                                            Cubic                               Matrix multiplcation
# O(2^n)                                            Exponential                         'Towers of Hanoi' problem, backtracking

# Constant Complexity
# The complexity of this algorithm is constant, O(1) as it only performs one operation regardless of the size of the input.
# Constant complexity is denoted by O(c), where c can be any constant number

def sumFirstTwo(input) :
    return input[0] + input [1]

print(sumFirstTwo((1, 2, 3, 4, 5)))

# Logarithmic Complexity
# The complexity of this algorithm is logarithmic, O(logn), since the value of i in the while loop grows(increments) logarithmically, the number of iterations is less than n.

def printAFew(input):
    i = 1
    while i < len(input):
        print(input[i])
        i *= 2
    
printAFew([input.randint(0,1000) for i in range(1, 1000001)])

# Quadratic Complexity
# The complexity of this algorithm is quadratic, O(n^2). For each iteration of the outer loop, the nested inner loop iterates n times. 
# The total number of iterations performed is n*n

def example(n):
    for i in range(n):
        for j in range(n):
            print(i * j)
example(5)

# Simplification Rules
    # Change non-zero coefficients to 1
        # When n become extremely large, the constant values become insignificant
    # Ignore low-order terms. High-order terms dominate the equation
        # 1 < logn < n < nlogn < n^2 < 2^n < n!



# Node
# A node is a basic unit of a data structure, such as a linked list or tree data structure.
# Nodes contain data and also may link to other notes. Links between nodes are often implemented by pointers.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
    def setNextNode(self, node) :
        self.next = node
    
    def getNextNode(self) :
        return self.next

    def __str__(self) :
        return str(self.data)

x = 'Happy'
y = 'Birthday'

node1 = Node(x)
node2 = Node(y)

node1.setNextNode(node2)

print(node1)
print(node1.getNextNode())


# Linked Lists

# A linked list is built from a collection of nodes, where each node is linked to another node.
# A linked list must maintain a reference to the first node in order to access the other nodes.

class LinkedList:
    def __init__(self) :
        self.head = None