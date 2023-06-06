def bubbleSort(self,arr, n):
        # code here
        for i in range(n):
            swapped=False
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            
            if swapped==False:
                return 
            
#Recursive
def bubble_sort_recursive(arr, n):
    # Base case: If there's only one element or the array is empty, it's already sorted
    if n == 1 or not arr:
        return arr

    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call on the remaining unsorted portion of the array
    return bubble_sort_recursive(arr, n - 1)


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

sorted_arr = bubble_sort_recursive(arr, n)

print("Sorted array:", sorted_arr)
