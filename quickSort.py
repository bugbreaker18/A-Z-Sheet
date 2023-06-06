def quickSort(self,arr,low,high):
        if(low<high):
            pidx = partition(arr, low, high)
            quickSort(arr, low, pidx -1)
            quickSort(arr, pidx+1, high)
    
def partition(self,arr,low,high):
    pivot = arr[0]
    i = low
    j = high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    return j