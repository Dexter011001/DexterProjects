#Binary search algorithm

def BinarySearch(arr,lower,upper,test):
	while lower <= upper:
		mid = lower + (upper-lower)//2

		if arr[mid] == test:
			return mid

		elif arr[mid] < test:
			lower = mid + 1

		elif arr[mid] > test:
			upper = mid - 1
	return -1

sorted_array = [0,20,42,45,70,100,225,226,230,231,290,300,323,329,330,341,346,389,400]
test = 341

result = BinarySearch(sorted_array,0,len(sorted_array)-1,test)

if result != -1:
	print("Found element: " + str(test) + " at index: " + str(result) )
else:
	print("Element is not present in array")






