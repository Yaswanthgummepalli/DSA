def swap(arr,a,b):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp
def partition(arr,start,end):
    pivot_index=start
    while start<end:
        while start < len(arr) and arr[start] <= arr[pivot_index]:
            start += 1
        while arr[end] > arr[pivot_index]:
            end -= 1
        if start < end:
            swap(arr, start, end)
    swap(arr,end,pivot_index)
    return end
def quicksort(arr,start,end):
    if start<end:
        pi = partition(arr, start, end)
        quicksort(arr, start, pi - 1)
        quicksort(arr, pi + 1, end)

if __name__=="__main__":
    arr = [11, 34, 12, 2, 4, 5, 6]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


