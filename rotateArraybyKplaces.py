arr = [1,2,3,4,5]
n = 5
k = 3
# Brute Forece 
# Left Rotation: 
def leftRotation(arr, n, k):
    k = k%n
    if k>n: 
        return
    temp = []*k
    for i in range(k):
        temp[i] = arr[i]
    for i in range(n-k):
        arr[i] = arr[i+k]
    for i in range(n-k, n):
        arr[i] = temp[i-n+k]
    print(arr)

# Right Rotation:
def rightRotation(arr, n,k):
    k = k%n
    temp = []*k
    for i in range(n-k, n):
        temp[i-n+k] = arr[i]
    for i in range(n-k-1, -1, -1):
        arr[i+k] = arr[i]
    for i in range(k):
        arr[i] = temp[i]
    print(arr)


    #Optimal

    # Reverse function:
    def Reverse(arr, start, end):
        while(start<=end):
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    
    def leftrotate(arr, n, k):
        # Reverse first k elements
        Reverse(arr, 0, k-1)
        # Reverse last k elements
        Reverse(arr, k, n-1)
        # Reverse entire array
        Reverse(arr, 0, n-1)

    def rightrotate(arr, n, k):
        # Reverse last k elements:
        Reverse(arr,n-k, n-1)
        # Reverse first n-k elements:
        Reverse(arr, 0, n-k-1)
        # Reverse entire array
        Reverse(arr, 0, n-1)