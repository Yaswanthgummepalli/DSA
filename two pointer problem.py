#finding the indices which add up equal to target
def sum(arr,target):

    for l in range(0,len(arr)-1):
        for i in range(l + 1, len(arr)):
            if arr[l] + arr[i] == target:
                print("indeces are",l, i)
                return True
    else:
        print("not found")
        return False
arr=[12,13,24,56,45,18]
target=30
print(sum(arr,target))

















