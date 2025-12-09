def insertionsort(elements):
    for i in range(1,len(elements)):
        pointer=elements[i]
        j=i-1
        while j>=0 and pointer<elements[j]:
            elements[j+1]=elements[j]
            j=j-1
        elements[j+1]=pointer

if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    insertionsort(elements)
    print(elements)
