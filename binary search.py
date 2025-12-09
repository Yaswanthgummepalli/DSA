
def binarysearch(list,n):
    l=0
    pos=-1
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==key:
            globals()['pos']=mid
            return True
        else:
            if list[mid]>key:
                u=mid-1
            else:
                l=mid+1
    return False
list=[12,13,14,15,16,17]
key=18
print(binarysearch(list,key))
