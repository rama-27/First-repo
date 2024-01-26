def insertionsort(l):
    for i in range(1,len(l)):
        j=i-1
        while(j>=0 and l[j]>l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
            j=j-1
    print(l)
def readlist():
    print("enter the elements in list with ,")
    li=list(map(int,input().split(',')))
    return li
list1=readlist()
insertionsort(list1)
        