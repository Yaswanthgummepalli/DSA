def selectionsort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(min_index+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
if __name__=="__main__":
    arr=[
        [1,2,3,4,5,6],
        [89,78,67,56,45],
        [12],
        []
    ]
    for i in arr:
        selectionsort(i)
        print(i)
