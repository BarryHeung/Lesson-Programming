# (12 Algorithms - 03 Bubble Sort and Insertion Sort)

# Lesson code 1

a = [7,4,6,8,1,5]

def bubble1():
    pass

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


swap(arr,0,1)
print(arr[0], arr[1])



# Lesson code 2

arr = [1, 4, 5, 6, 7, 8]

def bubble1(arr):
	swap = True
	while swap:
		swap = False
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]
				swap(arr,j,j+1)
				swap = True
				#end if



# My code

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if not swapped:
			return


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
