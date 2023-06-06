arr = [4,2,5,2,6,7,1]
n = 7

def selectionSort(arr, n):
    for i in range(0,n-2):
        mini = i
        for j in range(i, n-1):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini],arr[i] = arr[i], arr[mini]
    return arr
 
#using 2 functions: 
def select(self, arr, i):
    mini = i
    for idx in range(i+1,len(arr)):
        if arr[mini]>arr[idx]:
            mini = idx
    return mini
    
def selectionSort(self, arr,n):
    for i in range(n):
        idx = self.select(arr,i)
        arr[i],arr[idx] = arr[idx], arr[i]
    return arr
