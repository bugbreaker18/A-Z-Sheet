def mergeSort(arr, low, high):
    if(low >= high):
        return
    mid = (low + high)/2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, high, mid)

def merge(arr, low, high, mid):
    temp = []*len(arr)
    i = low
    j = high
    while(left <= mid and right <= high):
        if arr[i] <= arr[right]:
            temp.append(arr[i])
        else:
            temp.append(arr[j])
            i+= 1
    while(left<=mid):
        temp.append(arr[i])
        i+=1
    while(right<=high):
        temp.append(arr[j])
        j+=1
    for i in range(low, high):
        arr[i] = temp[i-low]
