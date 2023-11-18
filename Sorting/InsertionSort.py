def  insertionSort(arr):
	for  i in range(1,len(arr)):
		j=i
		while arr[j-1] > arr[j] and j > 0:
			arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1

if __name__ == "__main__":
	a = [2, 5, 4, 9, 1, 3 ]
	insertionSort(a)
	print(a)