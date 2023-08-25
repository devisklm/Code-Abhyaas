#progem to check whther the array is sorted or not
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a=a+[x]
issorted=False
if(a[0]<a[1]):
    for i in range(n-1):
        if(a[i]<a[i+1]):
            issorted=True
        if(a[i]>a[i+1]):
            issorted=False
            break
else:
    for i in range(n-1):
        if(a[i]>a[i+1]):
            issorted=True
        if(a[i]<a[i+1]):
            issorted=False
            break
if(issorted):
    print("The array is sorted")
else:
    print("The array is not sorted")
