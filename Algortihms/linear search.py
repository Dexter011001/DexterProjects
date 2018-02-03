#linear search algorithm

number = 341

array = [0,20,42,45,70,100,225,226,230,231,290,300,323,329,330,341,346,389,400]

for index,item in enumerate(array):
	if number == array[index]:
		print("Found number: " + str(item) + " at array location: " + str(index))
		break
	else:
		print("Number not found")
		
