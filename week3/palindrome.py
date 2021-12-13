class Stacks:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, e):
        self.top.insert(0, e)
    
    def pop(self):
        return self.top.pop()

    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.top == []

    def peek(self):
        return self.top[len(self.top)-1]



class Queues:
    def __init__(self):
        self.queue = []

    def enQueue(self, x):
        self.queue.append(x)
    
    def deQueue(self):
        data = self.queue.pop()
        return data

    def size(self):
        return self.queue

    def isEmpty(self):
        return self.queue
    
    def peek(self):
        if self.queue:
            return self.queue.data
        else:
            return None




def isPalindrome(x):
    return x == x[::-1]
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))