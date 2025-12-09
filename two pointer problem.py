#finding the indices which add up equal to target
def sum(arr,target):
    arr=sorted(arr)
    length=len(arr)
    left=0
    right=length-1
    res=[]
    while left<right:
        if arr[left]+arr[right]==target:
            res.append(left)
            res.append(right)
            return res
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1    
           
    return None         
           
arr=[3,2,4]
target=7
print(sorted(arr))
print(sum(arr,target))
















