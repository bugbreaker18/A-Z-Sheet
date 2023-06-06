def insert(self, alist, index, n):
        temp  = alist[index+1]
        while index >= 0 and alist[index]>temp: 
            alist[index+1]=alist[index] 
            index = index-1
        alist[index+1] = temp
    #Function to sort the list using insertion sort algorithm.    

def insertionSort(self, alist, n):
    for i in range(1,n):
        self.insert(alist,i-1,n)


#Recursive:
def insertion_sort_recursive(arr, n):
    # Base case: If there's only one element or the array is empty, it's already sorted
    if n <= 1 or not arr:
        return arr

    # Sort the first n-1 elements recursively
    insertion_sort_recursive(arr, n - 1)

    # Insert the last element into the sorted portion
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

insertion_sort_recursive(arr, n)

print("Sorted array:", arr)

