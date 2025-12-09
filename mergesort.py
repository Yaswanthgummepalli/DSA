def merging(a,b):

    s=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            s.append(a[i])
            i+=1
        else:
            s.append(b[j])
            j+=1
    while i<len(a):
        s.append(a[i])
        i+=1
    while j<len(b):
        s.append(b[j])
        j+=1

    return s
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergesort(left)
    right=mergesort(right)

    c=merging(left,right)
    return c
if __name__=="__main__":
    arr=[21,38,29,17,4,25,32,9]
    array=mergesort(arr)
    print(array)





