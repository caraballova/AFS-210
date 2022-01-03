# List Data Structure in Python

# Find an item in the list (Sequential or Linear Search) on Unordered List

def linear_search(list, term):
	list_size = len(list)
	for i in range(list_size):
		if term == list[i]:
			return True
	return False

myList = [11, 30, 25, 27, 9, 19, 28, 3, 21, 17]

print(linear_search(myList,4))


# Sequential (Linear) Search on Ordered List

def linear_search(list, term):
	list_size = len(list)
	for i in range(list_size):
		if term == list[i]:
			return True
		elif list[i] > term:
			return False
	return False

myList = [3, 9, 11, 17, 19, 21, 25, 27, 28, 30]

print(linear_search(myList,25))

# Bubble Sorting

# The bubble sort makes multiple passes through a list. 
# It compares adjacent items and exchanges those that are out of order. 
# Each pass through the list places the next largest value in its proper place. 
# In essence, each item “bubbles” up to the location where it belongs.

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
           
            print(a_list)
				
				
myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
bubble_sort(myList)
print()
print("Sorted Listed: ")
print(myList)

# Selection Sort

# The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
# In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. 
# As with a bubble sort, after the first pass, the largest item is in the correct place. 
# After the second pass, the next largest is in place. 
# This process continues and requires 𝑛 − 1 passes to sort 𝑛 items, since the final item must be in place after the (𝑛 − 1)st pass.

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location

        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp        		

        print(a_list)


myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
selection_sort(myList)
print()
print("Sorted Listed: ")
print(myList)


# Insertion Sort

# Insertion sort algorithm works by maintaining a sorted sublist in the lower positions of the list.  
# As a new item is found, it is inserted into the sorted sublist in the correct position. 
# The sorted sublist grows by one with each new item as the “unsorted” sublist shrinks by one.
# The time complexity of Insertion sort remains the same as bubble and selection sort at O(n^2)


def insertion_sort(a_list):
    passCount = 1
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

        print(passCount,"- ",a_list)
        passCount += 1



myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
insertion_sort(myList)
print()
print("Sorted Listed: ")
print(myList)

# Quick Sort

# Quick sort algorithm uses a divide and conquer technique.
# Requires selecting an efficient pivot point.  All the elements to be sorted will be compared with this pivot. Pivot should be roughly larger that half of the elements.
# Next, the elements are reordered such that all elements less than the pivot are to the left of the pivot and all elements greater than the pivot are to the right. 
# This is referred to as Partitioning.
# Next repeat the above steps recursively to elements smaller than the pivot.  
# Then recursively to the elements greater than the pivot.  
# The base case of the recursion is a single element.
# The time complexity of Quick sort is O(𝑛 log 𝑛) but may degrade to O(𝑛^2) if the pivot points are not near the middle of the list.

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partition(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        
def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high = high - 1
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
        else:
            break

    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
quick_sort(myList,0,len(myList)-1)
print()
print("Sorted Listed: ")
print(myList)
