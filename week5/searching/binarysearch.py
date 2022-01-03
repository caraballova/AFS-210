# Write the code to perform a binary search on a sorted list.  
# The function should #accept a sorted list and the value to search for as inputs.
# The function should return either True or False depending if the provided value was # found in the sorted list.

def binary_search(list, term):
	first = 0
	last = len(list)-1
	found = False
	while( first <= last and not found):
		mid = (first + last) // 2
		if list[mid] == term :
			found = True
		else:
			if term < list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
myList2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
myList3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(myList, 31))
print(binary_search(myList2, 77))
print(binary_search(myList3, "Delta"))